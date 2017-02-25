from django.shortcuts import render


# Get index.html
def get_index(request):
   return render(request, 'index.html')


# Get Our Team page
def get_ourteam(request):
   return render(request, 'ourteam.html')


# Get Contact Page
def get_contact(request):
   return render(request, 'contacts/contact.html')


# Get Contact Thank You Page
def get_contact_thanks(request):
   return render(request, 'contacts/contact_thanks.html')