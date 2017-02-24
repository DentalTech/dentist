from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Appointment
from .forms import AppointmentForm
from django.template.context_processors import csrf
from accounts.models import Family
from django import forms


def create_appointment(request):

    user = request.user

    AppointmentForm.base_fields['patient_name'] = forms.ModelChoiceField(
        queryset=Family.objects.filter(account_name_id=user.id))

    if user.is_authenticated:
        if request.method == 'POST':

            form = AppointmentForm(request.POST, instance=user)

            if form.is_valid():
                date = form.cleaned_data['appointment_date'],
                time = form.cleaned_data['appointment_time']
                patient_name = form.cleaned_data['patient_name']
                family = Family.objects.get(full_name=patient_name).id
                print('family: ' + str(family))

                appointment = Appointment()
                appointment.appointment_date = date[0]
                appointment.appointment_time = time
                appointment.patient_name_id = family
                appointment.save()

                print 'date is: ' + str(date[0])
                print 'time is: ' + str(time)
                print 'user is: ' + str(user.id)

                return redirect(reverse('appointments'))

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

    print user.id
    family = Family.objects.all()

    for item in family:
        print item

    all_family = Family.objects.filter(account_name_id=user.id)

    for item in all_family:
        print item.id

    for person in all_family:
        for appointment in appointments:
            print appointment.patient_name_id
            if appointment.patient_name_id == person.id:
                family_appointments.append(appointment)

        print family_appointments

    return render(request, "appointments/appointments.html", {"appointments": family_appointments})


