from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Appointment
from .forms import AppointmentForm
from django.template.context_processors import csrf
from accounts.models import Family
from django import forms
from django.db import IntegrityError
from django.contrib import messages


def create_appointment(request):

    user = request.user

    AppointmentForm.base_fields['patient_name'] = forms.ModelChoiceField(
        queryset=Family.objects.filter(account_name_id=user.id))

    if user.is_authenticated:
        if request.method == 'POST':

            form = AppointmentForm(request.POST, instance=user)

            if form.is_valid():
                try:
                    date = form.cleaned_data['appointment_date'],
                    time = form.cleaned_data['appointment_time']
                    patient_name = form.cleaned_data['patient_name']
                    family = Family.objects.get(full_name=patient_name).id

                    appointment = Appointment()
                    appointment.appointment_date = date[0]
                    appointment.appointment_time = time
                    appointment.patient_name_id = family
                    appointment.save()

                    return redirect(reverse('appointments'))

                except IntegrityError as e:
                    messages.error(request, "That patient already has an appointment")

        else:
            form = AppointmentForm()

        args = {}
        args.update(csrf(request))

        args['form']=form

        return render(request, 'appointments/create_appointment.html', args)


def get_user_appointments(request):

    user = request.user

    appointments = Appointment.objects.all()
    family_appointments = []

    all_family = Family.objects.filter(account_name_id=user.id)
    print all_family[0].full_name

    for person in all_family:
        for appointment in appointments:
            if appointment.patient_name_id == person.id:
                family_appointments.append(appointment)



    return render(request, "appointments/appointments.html", {"appointments": family_appointments})


