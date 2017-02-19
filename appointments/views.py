from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Appointment
from .forms import AppointmentForm
from django.template.context_processors import csrf


def create_appointment(request):

    user = request.user

    if user.is_authenticated:
        if request.method == 'POST':
            form = AppointmentForm(request.POST, instance=user)
            if form.is_valid():
                date = form.cleaned_data['appointment_date'],

                appointment = Appointment()
                appointment.appointment_date = date[0]
                appointment.patient_name_id = user.id
                appointment.save()

                print 'date is: ' + str(date[0])
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

