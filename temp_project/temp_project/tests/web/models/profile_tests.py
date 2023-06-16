from django.core.exceptions import ValidationError
from django.test import TestCase

from temp_project.web.models import TestProfile


class ProfileModelTests(TestCase):

    def test_profile_save__when_egn_is_valid__expect_correct_result(self):
        # Arrange
        profile = TestProfile(
            firs_name='Velin',
            last_name='Iliev',
            age=20,
            egn='1234567890'
        )
        # Act
        profile.full_clean()
        profile.save()
        # Assert
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_egn_has_9_digits__expect_validation_error(self):
        # Arrange
        profile = TestProfile(
            firs_name='Velin',
            last_name='Iliev',
            age=20,
            egn='123456789'
        )
        # Act
        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()
        # Assert
        self.assertIsNotNone(ve.exception)

    def test_profile_save__when_egn_has_11_digits__expect_validation_error(self):
        # Arrange
        profile = TestProfile(
            firs_name='Velin',
            last_name='Iliev',
            age=20,
            egn='12345678901'
        )
        # Act
        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()
        # Assert
        self.assertIsNotNone(ve.exception)
