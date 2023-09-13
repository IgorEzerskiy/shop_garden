from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class ImageValidator(BaseValidator):
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __call__(self, value):
        image_height = value.height
        image_width = value.width

        if image_width != self.width or image_height != self.height:
            raise ValidationError(f'The height or width is not equal to the specified {self.width}*{self.height}. '
                                  f'Yours {image_width}*{image_height}px.'
                                  )
