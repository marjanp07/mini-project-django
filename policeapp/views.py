from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'police/home.html')

def viewcomplaints(request):
    
    return render(request,'police/viewcomplaints.html')

def complaintdetails(request):
    
    return render(request,'police/complaintdetails.html')

def firupdate(request):
    
    return render(request,'police/firupdate.html')

