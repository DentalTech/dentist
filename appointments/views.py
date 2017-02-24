from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Appointment
from .forms import AppointmentForm
from django.template.context_processors import csrf
from accounts.models import Family


def create_appointment(request):

    user = request.user

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


def all_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "appointments/appointments.html", {"appointments": appointments})

