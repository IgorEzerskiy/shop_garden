from django.core.exceptions import ValidationError


def validate_image(image, height, width):
    image_height = image.height
    image_width = image.width

    if image_width != width or image_height != height:
        raise ValidationError(f'The height or width is not equal to the specified {width}*{height}. '
                              f'Yours {image_width}*{image_height}px.'
                              )
