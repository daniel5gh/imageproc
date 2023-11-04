import subprocess

import numpy as np


def generate_images(number_to_generate=10, width=512, height=512, depth=3):
    """yield images in numpy arrays with random noise"""

    for _ in range(number_to_generate):
        yield np.random.randint(0, 255, (width, height, depth), dtype=np.uint8)


def read_from_video(file_path):
    """generate images using ffmpeg"""
    command = [
        "ffmpeg",
        "-i",
        file_path,
        "-f",
        "image2pipe",
        "-pix_fmt",
        "rgb24",
        "-vcodec",
        "rawvideo",
        "-",
    ]
    # run ffmpeg command and get stdout as a byte stream
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # read stdout byte stream as numpy array
    while True:
        # read 1 frame
        raw_image = process.stdout.read(1280 * 720 * 3)
        if not raw_image:
            process.returncode = process.wait()
            if process.returncode:
                print(process.stderr.read().decode())
            break
        # convert to numpy array
        image = np.frombuffer(raw_image, dtype="uint8")
        # reshape to 720 image
        image = image.reshape((720, 1280, 3))
        # yield image
        yield image
