import cv2
from tqdm import tqdm


def save_images(images, destination, extension="png"):
    """save images to destination"""

    destination.mkdir(parents=True, exist_ok=True)

    for index, image in tqdm(enumerate(images), total=len(images)):
        cv2.imwrite(f"{destination}/image_{index}.{extension}", image)
