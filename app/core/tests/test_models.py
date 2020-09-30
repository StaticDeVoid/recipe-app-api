from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        # test creating a new user with email
        email = 'test@gmail.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # test the normalization of the new users email
        email = 'test@GMAIL.cOM'
        user = get_user_model().objects.create_user(email, 'teststests2312')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # tests that the creation of the user requires an email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_create_new_superuser(self):
        '''Testing the creation of a superuser'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)