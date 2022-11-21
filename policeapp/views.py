from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="userapp:login")
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
@login_required(login_url="userapp:login")
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
@login_required(login_url="userapp:login")
def complaintdetails(request,id):
    police_status_form= policecomplaintupdateForm(request.POST,request.FILES)
    user_statusform = complaintupdateForm(request.POST,request.FILES)
    firForm = FirCreateForm(request.POST,request.FILES)
    firRejectForm = FirrejectForm(request.POST,request.FILES)

    fir_detail=None
    complaint = complaints.objects.get(id=id)
    cstatuses = complaint_updates.objects.filter(complaint=complaint).order_by('date')
    if fir_details.objects.filter(complaint=complaint).exists():
        fir_detail=fir_details.objects.get(complaint=complaint)

    print(request.user)
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
        statusform=police_status_form
    else:
        statusform=user_statusform

    if statusform.is_valid():
        print("Status form Valid")
    if request.method =='POST':
        if firRejectForm.is_valid() and not statusform.is_valid() and not firForm.is_valid():
            print("Reject")
            fir = firRejectForm.save(commit=False)
            if fir_details.objects.filter().exists():
                newdid= fir_details.objects.filter().last().id+1
            else:
                newdid=1
            fir_id = 'FIR00'+str(newdid)
            fir.fir_number ='NA'
            fir.status='REJECTED'
            fir.staff = request.user
            fir.complaint = complaint
            fir.save()

        if request.user.is_staff and statusform.is_valid():
             print("point 1")
             cstatus=statusform.save(commit=False)
             cstatus.commented_by=request.user
             cstatus.complaint=complaint
             cstatus.save()
        elif statusform.is_valid():
            print("point 2")
            cstatus=statusform.save(commit=False)
            cstatus.commented_by=request.user
            cstatus.complaint=complaint
            cstatus.status='OPEN'
            cstatus.save()
        if firForm.is_valid() and not statusform.is_valid():
            print("point 3")
            fir = firForm.save(commit=False)
            fir.staff = request.user
            fir.complaint = complaint
            if fir_details.objects.filter().exists():
                newdid= fir_details.objects.filter().last().id+1
            else:
                newdid=1
            fir_id = 'FIR00'+str(newdid)
            fir.fir_number = fir_id

            fir.save()
        

    context={
        "is_police":request.user.is_staff,
        "statusform":statusform,
        "cstatuses":cstatuses,
        "complaint":complaint,
        "user_details":user_details,
        "firForm":firForm,
        "fir_detail":fir_detail,
        "firRejectForm":firRejectForm
    }
    return render(request,'people/casestatustimeline.html',context)

@login_required(login_url="userapp:login")
def firupdate(request,id):
    fir_detail=fir_details.objects.get(id=id)
    firupdateRecords=fir_status_report.objects.filter(fir=fir_detail)
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
    else:
        user_details=peoples.objects.get(user=request.user)
    firForm = FirUpdateForm(request.POST,request.FILES,instance=fir_detail)
    if request.method =='POST':
        old_fir_detail=fir_details.objects.get(id=id)
        if firForm.is_valid():
            newfirdetails=firForm.save()
            comment=''
            if newfirdetails.hearing_date != old_fir_detail.hearing_date:
                comment='Hearing Date Updated :'+str(newfirdetails.hearing_date)
            elif newfirdetails.decision_date != old_fir_detail.decision_date:
                comment='Decision Date Updated :'+str(newfirdetails.decision_date)
            elif newfirdetails.court_no_and_judge != old_fir_detail.court_no_and_judge:
                comment='Court No Updated :'+str(newfirdetails.court_no_and_judge)
            elif newfirdetails.status != old_fir_detail.status:
                comment='Status Updated to :'+str(newfirdetails.status)
            firupdateRecord = fir_status_report()
            firupdateRecord.fir=fir_detail
            firupdateRecord.comment=comment
            firupdateRecord.staff=request.user
            firupdateRecord.current_status=newfirdetails.status

            firupdateRecord.save()





    context={
        "user_details":user_details,
        "fir_detail":fir_detail,
        "firForm":firForm,
        "firupdateRecords":firupdateRecords,
    }
    return render(request,'people/viewfir.html',context)



@login_required(login_url="userapp:login")
def listfirs(request):
    if request.user.is_staff  and police_staff.objects.filter(user=request.user).exists():
        user_details=police_staff.objects.get(user=request.user)
        police_station=user_details.police_station
        fir_detailses = fir_details.objects.filter(complaint__police_station=police_station)
        context={
        'fir_detailses':fir_detailses,
        "user_details":user_details
        }
        return render(request,'people/myfir.html',context)
    else:
        return redirect('userapp:myfirs')