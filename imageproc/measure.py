import asyncio
import contextlib
import time
from concurrent.futures import ThreadPoolExecutor

import cv2
import numpy as np
import psutil
import tqdm


def generate_images(number_to_generate=10, width=512, height=512, depth=3):
    """yield images in numpy arrays with random noise"""

    for _ in range(number_to_generate):
        yield np.random.randint(0, 255, (width, height, depth), dtype=np.uint8)


def save_images(images, destination, extension="png"):
    """save images to destination"""

    destination.mkdir(parents=True, exist_ok=True)

    for index, image in tqdm.tqdm(enumerate(images), total=len(images)):
        cv2.imwrite(f"{destination}/image_{index}.{extension}", image)


def save_images_multithreaded(images, destination, extension="png"):
    """save images to destination"""

    with tqdm.tqdm(total=len(images)) as progress_bar:

        def update_progress_bar(*args):
            progress_bar.update(1)

        destination.mkdir(parents=True, exist_ok=True)

        with ThreadPoolExecutor() as executor:
            futures = []
            for index, image in enumerate(images):
                future = executor.submit(
                    cv2.imwrite,
                    f"{destination}/image_{index}.{extension}",
                    image,
                )
                future.add_done_callback(update_progress_bar)
                futures.append(future)
            for future in futures:
                future.result()


def save_images_asyncio(images, destination, extension="png"):
    """save images to destination"""

    # get main thread event loop
    loop = asyncio.get_event_loop()

    # not using tqdm.asyncio.tqdm because this method is not async itself
    with tqdm.tqdm(total=len(images)) as progress_bar:

        def update_progress_bar(*args):
            progress_bar.update(1)

        destination.mkdir(parents=True, exist_ok=True)

        # create tasks
        tasks = []
        for index, image in enumerate(images):
            task = loop.run_in_executor(
                None,
                cv2.imwrite,
                f"{destination}/image_{index}.{extension}",
                image,
            )
            task.add_done_callback(update_progress_bar)
            tasks.append(task)
        # wait for tasks to complete
        loop.run_until_complete(asyncio.wait(tasks))


@contextlib.contextmanager
def measure_performance(banner="", count=1):
    """context manager to measure performance"""

    # mutable object to store results
    result = []

    start_time = time.time()
    yield result
    end_time = time.time()
    time_taken = end_time - start_time
    extra = ""
    if count > 1:
        time_taken_per_iter = time_taken / count
        extra = f" ({time_taken_per_iter:.4f} seconds per iteration)"
    print(f"Execution time {banner}: {time_taken:.4f} seconds{extra}")
    result.append(time_taken)


def experiment1(args, output_path):
    # print basic machine specs from psutil
    print(f"CPU count: {psutil.cpu_count()}")
    print(f"CPU freq: {psutil.cpu_freq()}")
    load = psutil.getloadavg()
    print(f"current load {load}")
    print(f"writing to {output_path.absolute()}")

    with measure_performance(
        f"generate {args.number_to_generate} images", args.number_to_generate
    ):
        images = list(generate_images(**vars(args)))
    with measure_performance("save png images", args.number_to_generate) as t_png:
        save_images(images, output_path / "output_st")
    with measure_performance("save jpg images", args.number_to_generate) as t_jpg:
        save_images(images, output_path / "output_st", extension="jpg")
    with measure_performance(
        "save png images multi-threaded", args.number_to_generate
    ) as t_png_mt:
        save_images_multithreaded(images, output_path / "output_mt")
    with measure_performance(
        "save jpg images multi-threaded", args.number_to_generate
    ) as t_jpg_mt:
        save_images_multithreaded(images, output_path / "output_mt", extension="jpg")
    with measure_performance(
        "save png images multi-threaded", args.number_to_generate
    ) as t_png_async:
        save_images_multithreaded(images, output_path / "output_as")
    with measure_performance(
        "save jpg images multi-threaded", args.number_to_generate
    ) as t_jpg_async:
        save_images_multithreaded(images, output_path / "output_as", extension="jpg")
    # print performance improvements
    print(
        f"Multi-threaded PNG save is {t_png[0] / t_png_mt[0]:.2f} times faster than single threaded"
    )
    print(
        f"Multi-threaded JPG save is {t_jpg[0] / t_jpg_mt[0]:.2f} times faster than single threaded"
    )
    print(
        f"Asyncio PNG save is {t_png[0] / t_png_async[0]:.2f} times faster than single threaded"
    )
    print(
        f"Asyncio JPG save is {t_jpg[0] / t_jpg_async[0]:.2f} times faster than single threaded"
    )
