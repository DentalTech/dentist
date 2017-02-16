from django.shortcuts import render

# Get index.html
def get_index(request):
   return render(request, 'index.html')

# Get Our Team page
def get_ourteam(request):
   return render(request, 'ourteam.html')
