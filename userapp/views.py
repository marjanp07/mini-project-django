from django.shortcuts import render

# Create your views here.


def home(request):
    
    return render(request,'people/index.html')


def login(request):
    return render(request,'common/login.html')


def registeration(request):
    return render(request,'people/registeration.html')

def mycomplaints(request):
    return render(request,'people/mycomplaints.html')

def addcomplaints(request):
    return render(request,'people/addcomplaints.html')


def casestatustimeline(request):
    return render(request,'people/casestatustimeline.html')


def firstatuscheck(request):
    return render(request,'people/firstatuscheck.html')



def viewfir(request):
    return render(request,'people/viewfir.html')                    






    