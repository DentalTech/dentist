from django.test import TestCase, override_settings
from django.shortcuts import render_to_response
from .models import Subject

@override_settings(STATICFILES_STORAGE=None)
class SubjectPageTest(TestCase):

    fixtures = ['subjects', 'user']

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
                                                               Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)