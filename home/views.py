from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    person = {'name' : 'meysam'}
    return render(request, 'Home.html', context=person)

def new_user(request):
    user = {'username':'root'}
    return render(request, 'Newuser.html', context=user)
