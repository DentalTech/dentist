from __future__ import unicode_literals
from accounts.models import Family
from django.db import models
from datetime import date


class Appointment(models.Model):
    SLOT1 = '08:30'
    SLOT2 = '09:00'
    SLOT3 = '09:30'
    SLOT4 = '10:00'
    SLOT5 = '10:30'
    SLOT6 = '11:00'
    SLOT7 = '11:30'
    SLOT8 = '12:00'
    SLOT9 = '14:00'
    SLOT10 = '14:30'
    SLOT11 = '15:00'
    SLOT12 = '15:30'
    SLOT13 = '16:00'
    SLOT14 = '16:30'

    patient_name = models.ForeignKey(Family)
    appointment_date = models.DateField()
    appointment_time_choices = (
        (SLOT1, '08:30'),
        (SLOT2, '09:00'),
        (SLOT3, '09:30'),
        (SLOT4, '10:00'),
        (SLOT5, '10:30'),
        (SLOT6, '11:00'),
        (SLOT7, '11:30'),
        (SLOT8, '12:00'),
        (SLOT9, '14:00'),
        (SLOT10, '14:30'),
        (SLOT11, '15:00'),
        (SLOT12, '15:30'),
        (SLOT13, '16:00'),
        (SLOT14, '16:30'),
    )
    appointment_time = models.CharField(
        max_length=5,
        choices=appointment_time_choices,
        default=SLOT1,
    )

    def __unicode__(self):
        return str(self.appointment_date) + " - " + str(self.appointment_time) + " - " + str(self.patient_name)





