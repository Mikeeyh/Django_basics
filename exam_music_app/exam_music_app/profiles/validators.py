from django.core.exceptions import ValidationError


"""
We can write our custom validators here 
And just import them when we want to use them
"""


def validate_username(username):
    is_valid = all(ch.isalnum() or ch == '_' for ch in username)

    if not is_valid:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
