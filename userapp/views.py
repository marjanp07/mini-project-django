
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
    news_feed_list=[]
    print(request.user)
    if peoples.objects.filter(user=request.user).exists():
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
            print(userform.errors)
            print(personform.errors)
            context["errormessage"]= "User Already Registered"
   
    return render(request,'people/registeration.html',context)

@login_required(login_url="userapp:login")
def mycomplaints(request):
    
    complaints_list = complaints.objects.filter(user=request.user)
    context={
        'complaints_list':complaints_list
    }
    return render(request,'people/mycomplaints.html',context)


@login_required(login_url="userapp:login")
def addcomplaints(request):
    complaintform = complaintForm(request.POST,request.FILES)
    if request.method =='POST':
        if complaintform.is_valid():
            complaint=complaintform.save(commit=False)
            complaint.user=request.user
            complaint.save()

    context={
        "complaintform":complaintform
    }
    return render(request,'people/addcomplaints.html',context)

@login_required(login_url="userapp:login")
def casestatustimeline(request,id):
    police_status_form= policecomplaintupdateForm(request.POST,request.FILES)
    user_statusform = complaintupdateForm(request.POST,request.FILES)
    complaint = complaints.objects.get(id=id)
    cstatuses = complaint_updates.objects.filter(complaint=complaint).order_by('date')
    print(request.user)
    if request.user.is_staff:
        statusform=police_status_form
    else:
        statusform=user_statusform
    if request.method =='POST':
        if request.user.is_staff and statusform.is_valid():
             cstatus=statusform.save(commit=False)
             cstatus.commented_by=request.user
             cstatus.complaint=complaint
             cstatus.save()
        elif statusform.is_valid():
            cstatus=statusform.save(commit=False)
            cstatus.commented_by=request.user
            cstatus.complaint=complaint
            cstatus.status='OPEN'
            cstatus.save()


    context={
        "is_police":request.user.is_staff,
        "statusform":statusform,
        "cstatuses":cstatuses,
        "complaint":complaint
    }
    return render(request,'people/casestatustimeline.html',context)


def firstatuscheck(request):
    return render(request,'people/firstatuscheck.html')



def viewfir(request):
    return render(request,'people/viewfir.html')                    






    