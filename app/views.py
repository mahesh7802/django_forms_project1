from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def registration(request):
    RO=Registration()
    d={'RO':RO}
    if request.method=='POST':
        ROT=Registration(request.POST)
        if ROT.is_valid():
            name=ROT.cleaned_data['name']
            return HttpResponse(str(ROT.cleaned_data))
    return render(request,'registration.html',d)
