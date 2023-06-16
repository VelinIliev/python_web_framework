from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from temp_project.web.models import TestProfile

UserModel = get_user_model()


class BaseTestCase(TestCase):
    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)


class ProfileListViewTest(BaseTestCase):
    def test_profiles_list_view__when_no_profiles__expect_empty_list_and_count_context(self):
        response = self.client.get(reverse('test view'))
        # print(response.context)
        # print(response.template_name)
        self.assertCollectionEmpty([], response.context['testprofile_list'])
        self.assertEqual(0, response.context['profiles_count'])

    def test_profiles_list_view__when_profiles__expect_list_of_profiles_and_header(self):
        profiles = [
            TestProfile(firs_name="Velin", last_name='Iliev', age=20, egn='0123456789'),
            TestProfile(firs_name="Doncho", last_name='Minkov', age=21, egn='0123456789'),
        ]

        TestProfile.objects.bulk_create(profiles)

        response = self.client.get(reverse('test view'))
        # print(profiles)
        # print(list(response.context['testprofile_list']))
        self.assertEqual(profiles, list(response.context['testprofile_list']))
        self.assertEqual(2, response.context['profiles_count'])

    def test_profiles_list_view__when_anonymous_user__username_to_be_anonymous(self):
        response = self.client.get(reverse('test view'))
        # print(response.context['user'])
        self.assertEqual('AnonymousUser', str(response.context['user']))

    def test_profiles_list_view__when_loggedin_user__username_to_be_correct(self):
        credentials = {
            'email': 'doncho@mail.bg',
            'password': 'GoodPass123!',
        }

        user = UserModel.objects.create_user(**credentials)
        # print(user.pk)
        self.client.login(**credentials)

        response = self.client.get(reverse('test view'))
        # print(response.context['user'])
        self.assertEqual(credentials['email'], str(response.context['user']))

    def test_profiles_list_view__when_query_is_provided_expect_query_in_context(self):
        response = self.client.get(
            reverse('test view'),
            data={
                'query': 'the-query',
            })
        self.assertEqual('the-query', response.context['query'])

    def test_create_profile__when_user_is_loggedin__expect_to_create_profile(self):
        profile_data = {
            'firs_name': 'velin',
            'last_name': 'iliev',
            'age': 22,
            'egn': '0123456789',
        }
        credentials = {
            'email': 'velko@abv.bg',
            'password': 'GoodPass123!',
        }
        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.post(
            reverse('test profile create'),
            data=profile_data
        )

        created_profile = TestProfile.objects.filter(**profile_data).get()
        # print(created_profile)

        self.assertIsNotNone(created_profile)
        self.assertEqual(302, response.status_code)

    def test_create_profile__when_user_is_anonymous__expect_to_redirect_to_login(self):
        profile_data = {
            'firs_name': 'velin',
            'last_name': 'iliev',
            'age': 22,
            'egn': '0123456789',
        }

        response = self.client.post(
            reverse('test profile create'),
            data=profile_data
        )

        self.assertEqual(302, response.status_code)
        print(response.headers.get('Location'))
        expected_redirect = f'{settings.LOGIN_URL}?next={reverse("test profile create")}'
        self.assertEqual(expected_redirect, response.headers.get('Location'))
