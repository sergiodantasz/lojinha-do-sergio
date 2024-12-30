from io import BytesIO

from django.db.models.fields.files import ImageFieldFile
from PIL import Image


def resize_image(
    image: ImageFieldFile,
    max_size: tuple[int, int] = (800, 800),
    is_saved: bool = True,
):
    """Resizes the image to a specified size while maintaining the aspect ratio.

    Args:
        image (ImageFieldFile): Image object.
        max_size (tuple[int, int], optional): Maximum size that the image should have. If it is larger, it will be resized. Defaults to (800, 800).
        is_saved (bool, optional): True if the image is already saved, False if it is in memory. Defaults to True.
    """
    pil_image = Image.open(image.file)
    if pil_image.size <= max_size:
        return
    pil_image.thumbnail(max_size)
    if is_saved:
        pil_image.save(image.path)
        return
    buffer = BytesIO()
    pil_image.save(buffer, pil_image.format)
    buffer.seek(0)
    image.file.file = buffer
