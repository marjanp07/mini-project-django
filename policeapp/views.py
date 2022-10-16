from django.shortcuts import redirect, render
from .forms import *
# Create your views here.
def home(request):
    news_feed_list=[]
    user_details=None

    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        person_details=police_staff.objects.get(user=request.user)
        user_details=police_staff.objects.get(user=request.user)
        print(person_details.district)
        news_feed_list = news_feed.objects.filter(district=person_details.district)
    
        context={
            "news_feed_list":news_feed_list,
            "user_details":user_details
        }
    
        return render(request,'people/home.html',context)
    return redirect('userapp:userhome')

def viewcomplaints(request):
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
        police_station=user_details.police_station
        complaints_list = complaints.objects.filter(police_station=police_station)
        context={
        'complaints_list':complaints_list,
        "user_details":user_details
        }
        return render(request,'people/mycomplaints.html',context)
    else:
        return redirect('userapp:mycomplaints')

def complaintdetails(request,id):
    police_status_form= policecomplaintupdateForm(request.POST,request.FILES)
    user_statusform = complaintupdateForm(request.POST,request.FILES)
    complaint = complaints.objects.get(id=id)
    cstatuses = complaint_updates.objects.filter(complaint=complaint).order_by('date')
    print(request.user)
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
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
        "complaint":complaint,
        "user_details":user_details
    }
    return render(request,'people/casestatustimeline.html',context)

def firupdate(request):
    
    return render(request,'police/firupdate.html')

