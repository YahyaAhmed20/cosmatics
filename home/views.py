from django.shortcuts import render

# Create your views here.

def home(request):
    # Fetch the job list
   
    return render(request, 'home/home.html')