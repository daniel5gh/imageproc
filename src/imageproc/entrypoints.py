"""This module contains the entrypoint for the app"""
import argparse
from pathlib import Path

from imageproc.measure import (
    generate_images,
    measure_performance,
    save_images,
    save_images_multithreaded,
)


def measure():
    """Simple performance measuring of generate_images and save_images"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        default=1000,
        dest="number_to_generate",
        help="Number of images to generate. Default: 1000",
    )
    parser.add_argument(
        "-y",
        "--width",
        type=int,
        default=512,
        help="Width of the generated images. Default: 256",
    )
    parser.add_argument(
        "-x",
        "--height",
        type=int,
        default=512,
        help="Height of the generated images. Default: 256",
    )
    parser.add_argument(
        "-d",
        "--depth",
        type=int,
        default=3,
        help="Depth of the generated images. Default: 3",
    )
    args = parser.parse_args()

    with measure_performance(
        f"generate {args.number_to_generate} images", args.number_to_generate
    ):
        images = list(generate_images(**vars(args)))
    with measure_performance("save png images", args.number_to_generate) as t_png:
        save_images(images, Path("output_st"))
    with measure_performance("save jpg images", args.number_to_generate) as t_jpg:
        save_images(images, Path("output_st"), extension="jpg")

    with measure_performance(
        "save png images multi-threaded", args.number_to_generate
    ) as t_png_mt:
        save_images_multithreaded(images, Path("output_mt"))
    with measure_performance(
        "save jpg images multi-threaded", args.number_to_generate
    ) as t_jpg_mt:
        save_images_multithreaded(images, Path("output_mt"), extension="jpg")

    with measure_performance(
        "save png images multi-threaded", args.number_to_generate
    ) as t_png_async:
        save_images_multithreaded(images, Path("output_as"))
    with measure_performance(
        "save jpg images multi-threaded", args.number_to_generate
    ) as t_jpg_async:
        save_images_multithreaded(images, Path("output_as"), extension="jpg")

    # print performance improvements
    print(
        f"Multi-threaded PNG save is {t_png[0]/t_png_mt[0]:.2f} times faster than single threaded"
    )
    print(
        f"Multi-threaded JPG save is {t_jpg[0]/t_jpg_mt[0]:.2f} times faster than single threaded"
    )
    print(
        f"Asyncio PNG save is {t_png[0]/t_png_async[0]:.2f} times faster than single threaded"
    )
    print(
        f"Asyncio JPG save is {t_jpg[0]/t_jpg_async[0]:.2f} times faster than single threaded"
    )

    # clean up output directories
    Path("output_st").rmdir()
    Path("output_mt").rmdir()
    Path("output_as").rmdir()


if __name__ == "__main__":
    measure()
