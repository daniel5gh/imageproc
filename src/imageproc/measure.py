import contextlib
import time

import cv2
import numpy as np


def generate_images(number_to_generate=10, width=512, height=512, depth=3):
    """yield images in numpy arrays with random noise"""

    for _ in range(number_to_generate):
        yield np.random.randint(0, 255, (width, height, depth), dtype=np.uint8)


def save_images(images, destination, extension="png"):
    """save images to destination"""

    destination.mkdir(parents=True, exist_ok=True)

    for index, image in enumerate(images):
        cv2.imwrite(f"{destination}/image_{index}.{extension}", image)


@contextlib.contextmanager
def measure_performance(banner="", count=1):
    """context manager to measure performance"""

    start_time = time.time()
    yield
    end_time = time.time()
    time_taken = end_time - start_time
    extra = ""
    if count > 1:
        time_taken_per_iter = time_taken / count
        extra = f" ({time_taken_per_iter:.4f} seconds per iteration)"
    print(f"Execution time {banner}: {time_taken:.4f} seconds{extra}")
    return time_taken
