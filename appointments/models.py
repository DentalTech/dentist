from __future__ import unicode_literals
from django.utils import timezone
from accounts.models import User


from django.db import models

class Appointment(models.Model):

    patient_name = models.ForeignKey(User)
    appointment_date = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return str(self.appointment_date) + " - " + str(self.patient_name)




