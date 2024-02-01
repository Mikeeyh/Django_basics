'''
Django wants a callable  with a single arg that
raise a ValidationError if data is invalid
'''

from django.core.exceptions import ValidationError


def validate_email(email):  # Creating VALIDATOR Method 1:
    if '@' not in email:
        raise ValidationError('Email is invalid')


class FileSizeValidator:  # Creating VALIDATOR Method 2:
    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        if value.size > self.max_file_size:
            raise ValidationError(f'The size of the file should be less than {self.max_file_size}')


validate_email('mike@gmail.com')
# FileSizeValidator(5)(file)
