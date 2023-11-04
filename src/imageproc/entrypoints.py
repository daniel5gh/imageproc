"""This module contains the entrypoint for the app"""
import argparse
from pathlib import Path

from imageproc.measure import generate_images, measure_performance, save_images


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
    with measure_performance("save png images", args.number_to_generate):
        save_images(images, Path("output"))
    with measure_performance("save jpg images", args.number_to_generate):
        save_images(images, Path("output"), extension="jpg")


if __name__ == "__main__":
    measure()
