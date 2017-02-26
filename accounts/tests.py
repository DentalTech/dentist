from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings


class CustomUserTest(TestCase):
    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    def test_registration_form_with_one_family_member(self):
        form = UserRegistrationForm({
            'number_family': '1',
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'family_1': 'Test Name',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2018
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_with_multiple_family_members(self):
        form = UserRegistrationForm({
            'number_family': '3',
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'family_1': 'Test Name',
            'family_2': 'My Name',
            'family_3': 'Your Name',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2018
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())