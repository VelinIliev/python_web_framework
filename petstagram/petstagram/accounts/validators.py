from django.core.exceptions import ValidationError


def validate_only_letter(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Only letters are allowed')

