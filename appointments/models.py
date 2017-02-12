from __future__ import unicode_literals
from django.utils import timezone
from django.conf import settings
from services.models import Service


from django.db import models

class Appointment(models.Model):

    date = models.DateTimeField(default=timezone.now)
    patient_name = models.ForeignKey(settings.AUTH_USER_MODEL)
    service_name = models.ForeignKey(Service)


