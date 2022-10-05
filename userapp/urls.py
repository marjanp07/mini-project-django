
from .views import mycomplaints, home,login,registeration,addcomplaints,casestatustimeline,firstatuscheck,viewfir
from django.urls import path

app_name="userapp"

urlpatterns = [
    path('', home,name="userhome"),
    path('login/', login,name="login"),
    path('registeration/', registeration,name="registeration"),
    path('mycomplaints/', mycomplaints,name="mycomplaints"),
    path('addcomplaints/', addcomplaints,name="addcomplaints"),
    path('casestatustimeline/', casestatustimeline,name="casestatustimeline"),
    path('firstatuscheck/', firstatuscheck,name="firstatuscheck"),
    path('viewfir/', viewfir,name="viewfir"),

] 
