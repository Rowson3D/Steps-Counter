import os
from PIL import Image

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

def count_images_recursively(directory):
    """
    Counts image files recursively within a directory.

    Args:
        directory (str): The path to the directory to search.

    Returns:
        int: The total number of image files found.
    """
    image_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                image_count += 1
    return image_count