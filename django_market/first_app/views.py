from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return render(request, 'first_app/shop.html')

def support(request):
    return render(request, 'first_app/support.html')

def logout(request):
    return render(request, 'first_app/logout.html')

def developers(request):
    return render(request, 'first_app/developers.html')

def signin(request):
    return render(request, 'first_app/signin.html')

def tin_can(request):
    return render(request, 'first_app/tin_can.html')

def dorfromantik(request):
    return render(request, 'first_app/dorfromantik.html')

def gapr(request):
    return render(request, 'first_app/game_of_proj.html')




