
from .views import profile,myprofile,mycomplaints,myfirs,logout_view,index, home,login,registeration,addcomplaints,casestatustimeline,firstatuscheck,viewfir
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
    path('viewfir/<int:id>', viewfir,name="viewfir"),
    path('myfirs/', myfirs,name="myfirs"),
    path('myprofile/', myprofile,name="myprofile"),
    path('profile/<str:email>', profile,name="profile"),

] 
