import numpy as np


def generate_images(number_to_generate=10, width=512, height=512, depth=3):
    """yield images in numpy arrays with random noise"""

    for _ in range(number_to_generate):
        yield np.random.randint(0, 255, (width, height, depth), dtype=np.uint8)

