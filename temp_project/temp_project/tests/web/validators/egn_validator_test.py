from unittest import TestCase

from django.core.exceptions import ValidationError

from temp_project.web.validators import egn_validator


class EgnValidatorTests(TestCase):
    def test_when_valid__expect_ok(self):
        egn_validator('1234567890')

    def test_when_9digits__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            egn_validator('123456789')
        self.assertIsNotNone(ve.exception)

    def test_when_11digits__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            egn_validator('12345678901')
        self.assertIsNotNone(ve.exception)

    def test_when_none__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            egn_validator('')
        self.assertIsNotNone(ve.exception)

    def test_when_none_digits__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            egn_validator('123456s789')
        self.assertIsNotNone(ve.exception)
