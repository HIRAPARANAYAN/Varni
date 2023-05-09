from django.shortcuts import render

def Dashboard(request):
    return render(request,'adminDashboard/index.html')

def Search(request):
    return render(request,'adminDashboard/Search.html')
def Digitalbloan(request):
    return render(request,'adminDashboard/Digitalbloan.html')
def Digitalploan(request):
    return render(request,'adminDashboard/Digitalploan.html')
def Premiumploan(request):
    return render(request,'adminDashboard/Premiumploan.html')
def Premiumbloan(request):
    return render(request,'adminDashboard/Premiumbloan.html')
def Customers(request):
    return render(request,'adminDashboard/Customers.html')
def Createaccount(request):
    return render(request,'adminDashboard/Createaccount.html')
def Cardoffer(request):
    return render(request,'adminDashboard/Cardoffer.html')
def Specialoffer(request):
    return render(request,'adminDashboard/Specialoffer.html')
def Bumperoffer(request):
    return render(request,'adminDashboard/Bumperoffer.html')
def Staroffer(request):
    return render(request,'adminDashboard/Staroffer.html')

