from concurrent.futures import ThreadPoolExecutor

import cv2
from tqdm import tqdm


def save_images_multithreaded(images, destination, extension="png"):
    """save images to destination"""

    with tqdm(total=len(images)) as progress_bar:

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
            executor.shutdown(wait=True)


