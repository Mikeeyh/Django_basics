from django.core.validators import MinValueValidator
from django.db import models

from exam_music_app.profiles.models import Profile


# class Genre(models.TextChoices):
#     GENRE_POP = "Pop music"
#     GENRE_JAZZ = "Jazz music"
#     GENRE_ROCK = "Rock music"
#     GENRE_COUNTRY = "Country music"
#     GENRE_RNB = "R&B music"
#     GENRE_DANCE = "Dance music"
#     GENRE_HIP_HOP = "Hip Hop music"
#     GENRE_OTHER = "Other"


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_NAME_LENGTH = 30
    MAX_GENRE_LENGTH = 30
    MIN_PRICE = 0.0

    # TO be DELETED IF we use 2nd way
    GENRE_POP_MUSIC = "Pop music"
    GENRE_JAZZ_MUSIC = "Jazz music"
    GENRE_ROCK_MUSIC = "Rock music"
    GENRE_COUNTRY_MUSIC = "Country music"
    GENRE_RNB_MUSIC = "R&B music"
    GENRE_DANCE_MUSIC = "Dance music"
    GENRE_HIP_HOP_MUSIC = "Hip Hop music"
    GENRE_OTHER = "Other"

    # Including the genres to our model to use them in 'genre' -> choices=GENRES,
    # TO be DELETED IF we use 2nd way
    GENRES = (
        (GENRE_POP_MUSIC, GENRE_POP_MUSIC),
        (GENRE_JAZZ_MUSIC, GENRE_JAZZ_MUSIC),
        (GENRE_ROCK_MUSIC, GENRE_ROCK_MUSIC),
        (GENRE_COUNTRY_MUSIC, GENRE_COUNTRY_MUSIC),
        (GENRE_RNB_MUSIC, GENRE_RNB_MUSIC),
        (GENRE_DANCE_MUSIC, GENRE_DANCE_MUSIC),
        (GENRE_HIP_HOP_MUSIC, GENRE_HIP_HOP_MUSIC),
        (GENRE_OTHER, GENRE_OTHER),
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name:"  # we can rename the 'Name:' to 'Album Name: (this is shown in the browser page)
    )

    artist_name = models.CharField(
        max_length=MAX_ARTIST_NAME_LENGTH,
        null=False,
        blank=False,
        verbose_name="Artist:",
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL:",
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
        on_delete=models.CASCADE,  # to delete the albums after deleting the profile
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRES,  # 2nd way: choices=Genre.choices,
        null=False,
        blank=False,
    )
