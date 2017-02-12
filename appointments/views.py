from django.shortcuts import render
from .models import Appointment

# Create your views here.
def all_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "appointments/appointments.html", {"appointments": appointments})
