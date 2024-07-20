from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Home.html')

def new_user(request):
    return render(request, 'Newuser.html')
