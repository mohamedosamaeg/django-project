from django.http import HttpResponse
from django.shortcuts import render

def webgeo(request):
    return render(request,'geography.html')