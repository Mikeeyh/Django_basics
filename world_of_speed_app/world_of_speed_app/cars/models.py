from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed_app.profiles.models import Profile


def validate_year_range(year):
    if year < 1999 or year > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_CAR_MODEL_LENGTH = 15
    MIN_CAR_MODEL_LENGTH = 1
    MIN_PRICE = 1.0

    TYPE_RALLY = "Rally"
    TYPE_ONE_WHEEL = "Open-wheel"
    TYPE_KART = "Kart"
    TYPE_DRAG = "Drag"
    TYPE_OTHER = "Other"

    TYPES = (
        (TYPE_RALLY, TYPE_RALLY),
        (TYPE_ONE_WHEEL, TYPE_ONE_WHEEL),
        (TYPE_KART, TYPE_KART),
        (TYPE_DRAG, TYPE_DRAG),
        (TYPE_OTHER, TYPE_OTHER),
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_CAR_MODEL_LENGTH,
        validators=(
            MinLengthValidator(MIN_CAR_MODEL_LENGTH),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        editable=False,
    )
