from django.shortcuts import render, redirect
from django.http import HttpResponse    

# filepath: c:\Users\RELIANCE HEALTH\OneDrive - Reliance Health Inc\Desktop\Food Online\FoodOnline_main\views.py
def home(request):
    return render(request, 'home.html')

from datetime import datetime
def home(request):
    return render(request, 'home.html', {'timestamp': datetime.now().timestamp()})
