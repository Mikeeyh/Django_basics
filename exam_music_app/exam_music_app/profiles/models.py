from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# from exam_music_app.profiles.validators import validate_username


def validate_username(username):  # IF we use it from validators.py we should remove this code
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(
            MinLengthValidator(MIN_USERNAME_LENGTH),
            # validate_username, # -> ADDING THIS IF WE USE THE VALIDATOR FROM OUR validators.py
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
