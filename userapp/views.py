
from django.shortcuts import redirect, render
from .forms import *
from core.models import *
from django.contrib.auth import login as auth_login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    if request.user:
        return redirect('userapp:userhome')
    news_feed_list = news_feed.objects.all()

    context={
        "news_feed_list":news_feed_list
    }
    
    return render(request,'people/index.html',context)


@login_required(login_url="userapp:login")
def home(request):
    news_feed_list=[]
    user_details=None

    if not request.user.is_staff  and peoples.objects.filter(user=request.user).exists():
        person_details=peoples.objects.get(user=request.user)
        user_details=peoples.objects.get(user=request.user)
        print(person_details.district)
        news_feed_list = news_feed.objects.filter(district=person_details.district)
    
        context={
            "news_feed_list":news_feed_list,
            "user_details":user_details
        }
    
        return render(request,'people/home.html',context)
    return redirect('policeapp:policehome')


def login(request):
    context={}
    if request.method =='POST':
        print("POST")
        email=request.POST.get("email")
        print(email)
        password=request.POST.get("password")
        if email is not '' and password is not '':
            user = authenticate(request,username=email,password=password)
            if user is not None:
                auth_login(request,user)
                if user.is_staff:
                    return redirect('policeapp:policehome')
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
            
            user=User.objects.create_user(request.POST.get('username'),request.POST.get('password'))
            person=personform.save(commit=False)
            person.user=user
            person.save()
            return redirect("userapp:login")
        else :
            print(userform.errors)
            print(personform.errors)
            context["errormessage"]= "User Already Registered"
            
    return render(request,'people/registeration.html',context)

@login_required(login_url="userapp:login")
def mycomplaints(request):
    if not request.user.is_staff  and peoples.objects.filter(user=request.user).exists():
        user_details=peoples.objects.get(user=request.user)
    
        complaints_list = complaints.objects.filter(user=request.user)
        context={
            'complaints_list':complaints_list,
            "user_details":user_details
        }
        return render(request,'people/mycomplaints.html',context)
    else:
        return redirect('policeapp:viewcomplaints')
        


@login_required(login_url="userapp:login")
def addcomplaints(request):
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)
    
    complaintform = complaintForm(request.POST,request.FILES)
    if request.method =='POST':
        if complaintform.is_valid():
            complaint=complaintform.save(commit=False)
            complaint.user=request.user
            complaint.save()

    context={
        "complaintform":complaintform,
        "user_details":user_details
    }
    return render(request,'people/addcomplaints.html',context)

@login_required(login_url="userapp:login")
def casestatustimeline(request,id):
    police_status_form= policecomplaintupdateForm(request.POST,request.FILES)
    user_statusform = complaintupdateForm(request.POST,request.FILES)
    complaint = complaints.objects.get(id=id)
    cstatuses = complaint_updates.objects.filter(complaint=complaint).order_by('date')
    print(request.user)
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
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

    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)
    

    context={
        "is_police":request.user.is_staff,
        "statusform":statusform,
        "cstatuses":cstatuses,
        "complaint":complaint,
        "user_details":user_details
    }
    return render(request,'people/casestatustimeline.html',context)

@login_required(login_url="userapp:login")
def firstatuscheck(request):

    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)
    
    context={
        "user_details":user_details
    }
    return render(request,'people/firstatuscheck.html',context)




@login_required(login_url="userapp:login")
def viewfirs(request):
    if request.user  and peoples.objects.filter(user=request.user).exists():
        user_details=peoples.objects.get(user=request.user)
        police_station=user_details.police_station
        fir_detailses = fir_details.objects.filter(complaint__user=request.user)
        context={
        'fir_detailses':fir_detailses,
        "user_details":user_details
        }
        return render(request,'people/viewfir.html',context)
    else:
        return redirect('policeapp:listfir')

                   

def logout_view(request):
    logout(request)
    return redirect('userapp:userhome')



@login_required(login_url="userapp:login")
def myfirs(request):
    if request.user  and peoples.objects.filter(user=request.user).exists():
        user_details=peoples.objects.get(user=request.user)
        fir_detailses = fir_details.objects.filter(complaint__user=request.user)
        context={
        'fir_detailses':fir_detailses,
        "user_details":user_details
        }
        return render(request,'people/myfir.html',context)
    else:
        return redirect('polceapp:listfirs')


@login_required(login_url="userapp:login")
def viewfir(request,id):
    fir_detail=fir_details.objects.get(id=id)
    firupdateRecords=fir_status_report.objects.filter(fir=fir_detail)
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)

    context={
        "user_details":user_details,
        "fir_detail":fir_detail,
        "firForm":None,
        "firupdateRecords":firupdateRecords,
    }
    return render(request,'people/viewfir.html',context)

@login_required(login_url="userapp:login")
def myprofile(request):
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)
        selected_user=peoples.objects.get(user=request.user)
    context={
        "user_details":user_details,
        "selected_user":user_details,
    }
    return render(request,'people/profile.html',context)
 

@login_required(login_url="userapp:login")
def profile(request,id):
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
        selected_user = peoples.objects.get(user__id=id)
    else:
        user_details=peoples.objects.get(user=request.user)
        selected_user = peoples.objects.get(user__id=id)

    context={
        "user_details":user_details,
        "selected_user":selected_user,
    }
    return render(request,'people/profile.html',context)
 


