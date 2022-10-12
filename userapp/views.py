
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import *
from core.models import *
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):

    news_feed_list = news_feed.objects.all()

    context={
        "news_feed_list":news_feed_list
    }
    
    return render(request,'people/index.html',context)


@login_required(login_url="userapp:login")
def home(request):
    print(request.user)
    person_details=peoples.objects.get(user=request.user)
    print(person_details.district)
    news_feed_list = news_feed.objects.filter(district=person_details.district)

    context={
        "news_feed_list":news_feed_list
    }
    
    return render(request,'people/home.html',context)


def login(request):
    context={}
    if request.method =='POST':
        print("POST")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if email is not '' and password is not '':
            user = authenticate(request,email=email,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('userapp:userhome')
            else:
                context["errormessage"] = "User Name or password incorrect"
        else:
            context["errormessage"] = "Please enter User name and Password"

    return render(request,'common/login.html',context)


def registeration(request):
    userform = UserForm(request.POST,request.FILES)
    personform = PersonForm(request.POST,request.FILES)
    context={
        "userform":userform,
        "personform":personform

    }
    if request.method =='POST':
        if userform.is_valid() and personform.is_valid():
            # Validation required
            
            user=User.objects.create_user(request.POST.get('email'),request.POST.get('password'))
            person=personform.save(commit=False)
            person.user=user
            person.save()
        else :
             context["errormessage"]= "User Already Registered"
   
    return render(request,'people/registeration.html',context)

def mycomplaints(request):
    return render(request,'people/mycomplaints.html')

def addcomplaints(request):
    complaintform = complaintForm(request.POST,request.FILES)
    if request.method =='POST':
        if complaintform.is_valid():
            complaintform.save()

    context={
        "complaintform":complaintform
    }
    return render(request,'people/addcomplaints.html',context)


def casestatustimeline(request):
    return render(request,'people/casestatustimeline.html')


def firstatuscheck(request):
    return render(request,'people/firstatuscheck.html')



def viewfir(request):
    return render(request,'people/viewfir.html')                    






    