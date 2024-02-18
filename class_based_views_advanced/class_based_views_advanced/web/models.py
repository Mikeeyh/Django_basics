from django.db import models
from django.utils.text import slugify

# from our get_random_hash()
import uuid


def get_random_hash():  # function gives us random symbols
    return uuid.uuid4().hex[-4:]  # returning last 4 symbols


def generate_slug(*args, **kwargs):
    return get_random_hash()


# def generate_slug(*args, **kwargs):
#     while True:
#         slug = get_random_hash()  # Generate a random hash
#         if not Todo.objects.filter(slug=slug).exists():  # Check if the slug is unique
#             return slug  # Return the unique slug


class Todo(models.Model):
    MAX_TITLE_LENGTH = 24
    MAX_TENANT_LENGTH = 16

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField()

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    # Adding slug for example
    slug = models.SlugField(
        editable=False,
        # default=generate_slug,
    )

    tenant = models.CharField(
        max_length=MAX_TENANT_LENGTH,
        null=True,
        blank=True,
        default=None,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + get_random_hash()
        return super().save(*args, **kwargs)

