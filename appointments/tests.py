from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings


class AppointmentsTest(TestCase):

    def setUp(self):
        super(AppointmentsTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='letmein')
        self.assertEqual(self.login, True)


# Didn't have time to finish the tests
