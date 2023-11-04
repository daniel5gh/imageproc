import asyncio

import cv2
import tqdm.asyncio


async def save_image_async(image, file_path):
    """save single image

    basically same as single threaded version, cv2 does not support async. Also,
    we expect imwrite to be cpu bound, so we don't gain much from async.
    """

    cv2.imwrite(file_path, image)


async def save_images_async(images, destination, extension="png"):
    """save images to destination"""

    destination.mkdir(parents=True, exist_ok=True)

    tasks = []
    for index, image in enumerate(images):
        task = save_image_async(
            image, f"{destination}/image_{index}.{extension}"
        )
        tasks.append(task)

    # use tqdm gather to show progress bar
    await tqdm.asyncio.tqdm.gather(*tasks)


def save_images_in_asyncio_loop(images, destination, extension="png"):
    """get event loop and run async function"""

    # get main thread event loop
    loop = asyncio.get_event_loop()
    # and run the async function
    loop.run_until_complete(save_images_async(images, destination, extension))

