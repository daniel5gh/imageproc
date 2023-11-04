import contextlib
import time

import psutil

from .image_sources import generate_images, read_from_video
from .simple_save_async import save_images_in_asyncio_loop
from .simple_save_single_thead import save_images
from .simple_save_threadpool import save_images_multithreaded


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

    if not args.video:
        with measure_performance(
            f"generate {args.number_to_generate} images", args.number_to_generate
        ):
            images = list(generate_images(**vars(args)))
    else:
        with measure_performance("read video"):
            # make iterator that creates a new generator every time
            class VideoIterator:
                def __iter__(self):
                    return read_from_video("input/charge_teaser06wide-720p.mp4")
            images = VideoIterator()

    with measure_performance("save png images", args.number_to_generate) as t_png:
        save_images(images, output_path / "output_st")
    with measure_performance("save jpg images", args.number_to_generate) as t_jpg:
        save_images(images, output_path / "output_st", extension="jpg")
    with measure_performance(
        "save png images ThreadPoolExecutor", args.number_to_generate
    ) as t_png_mt:
        save_images_multithreaded(images, output_path / "output_mt")
    with measure_performance(
        "save jpg images ThreadPoolExecutor", args.number_to_generate
    ) as t_jpg_mt:
        save_images_multithreaded(images, output_path / "output_mt", extension="jpg")
    with measure_performance(
        "save png images asyncio", args.number_to_generate
    ) as t_png_async:
        save_images_in_asyncio_loop(images, output_path / "output_as")
    with measure_performance(
        "save jpg images asyncio", args.number_to_generate
    ) as t_jpg_async:
        save_images_in_asyncio_loop(images, output_path / "output_as", extension="jpg")
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
