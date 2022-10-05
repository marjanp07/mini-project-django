from multiprocessing import context
from django.shortcuts import render
from .forms import *

# Create your views here.


def home(request):
    
    return render(request,'people/index.html')


def login(request):
    return render(request,'common/login.html')


def registeration(request):
    userform = UserForm(request.POST,request.FILES)
    personform = PersonForm(request.POST,request.FILES)
    if request.method =='GET':
        print("Page Loaded")
    if request.method =='POST':
        print("Page Submitted")
    context={
        "userform":userform,
        "personform":personform

    }
    return render(request,'people/registeration.html',context)

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






    