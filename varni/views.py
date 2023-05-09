from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html',{'navname':'index'})

def company(request):
    return render(request, 'company.html',{'navname':'company'})

def contactus(request):
    return render(request, 'contactus.html',{'navname':'contactus'})

def marvel(request):
    return render(request, 'marvel.html',{'navname':'marvel'})

def universal(request):
    return render(request, 'universal.html',{'navname':'universal'})

def digitalloan(request):
    return render(request, 'digitalloan.html',{'navname':'digitalloan'})

