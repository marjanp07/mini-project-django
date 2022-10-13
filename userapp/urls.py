
from .views import mycomplaints,logout_view,index, home,login,registeration,addcomplaints,casestatustimeline,firstatuscheck,viewfir
from django.urls import path

app_name="userapp"

urlpatterns = [
    path('', index,name="index"),
    path('home/', home,name="userhome"),
    path('login/', login,name="login"),
    path('logout/', logout_view,name="logout"),
    path('registeration/', registeration,name="registeration"),
    path('mycomplaints/', mycomplaints,name="mycomplaints"),
    path('addcomplaints/', addcomplaints,name="addcomplaints"),
    path('casestatustimeline/<int:id>', casestatustimeline,name="casestatustimeline"),
    path('firstatuscheck/', firstatuscheck,name="firstatuscheck"),
    path('viewfir/', viewfir,name="viewfir"),

] 
