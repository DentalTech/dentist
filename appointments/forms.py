from django import forms
from appointments.models import Appointment
from django.views.generic.edit import CreateView


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['patient_name']
