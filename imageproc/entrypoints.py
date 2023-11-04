"""This module contains the entrypoint for the app"""
import argparse
import tempfile
from pathlib import Path

from .measure import experiment1


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

    with tempfile.TemporaryDirectory(dir="", prefix="output") as tmp_dirname:
        experiment1(args, Path(tmp_dirname))


if __name__ == "__main__":
    measure()
