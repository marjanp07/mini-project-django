
from .views import home,viewcomplaints,complaintdetails,firupdate
from django.urls import path

app_name="policeapp"

urlpatterns = [
    path('', home,name="policehome"),
    path('viewcomplaints/', viewcomplaints,name="viewcomplaints"),
    path('complaintdetails/<int:id>', complaintdetails,name="complaintdetails"),
    path('firupdate/<int:id>', firupdate,name="firupdate"),
] 
