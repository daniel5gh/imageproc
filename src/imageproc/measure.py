import contextlib
import time
from concurrent.futures import ThreadPoolExecutor

import cv2
import numpy as np
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
    print(f"\nExecution time {banner}: {time_taken:.4f} seconds{extra}")
    result.append(time_taken)
