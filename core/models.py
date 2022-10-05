from tabnanny import verbose
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create Save a User"""
        if not email:
            raise ValueError('User must have a Email')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user:
            return user

    def create_superuser(self, email, password):
        """Create and Save a super User"""
        user = self.model(email=email)
        user.set_password(password)
        user.name="admin"
        user.save(using=self.db)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """"Custom Model"""
    email = models.EmailField(max_length=225, unique=True)
    name=models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural="1.App Users"

class police_station(models.Model):
    name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    phone_number = models.IntegerField()

    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name_plural="2.Police station"


class police_staff(models.Model):
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    person_name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    post = models.CharField(max_length=225) 
    phone_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to="people/")

    def __str__(self):
        return str(self.user)


    class Meta:
        verbose_name_plural="3.Police Staff"
    

class peoples(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    police_station_range= models.ForeignKey(police_station,on_delete=models.PROTECT)
    person_name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    post = models.CharField(max_length=225) 
    adhar_number = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to="people/")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural="4.Peoples"


class complaints(models.Model):
    user = models.ForeignKey(peoples,on_delete=models.PROTECT)
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    complaint_discription = models.CharField(max_length=225)
    document_feild = models.FileField(upload_to="complaints/")
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural="5.Complaints"



class complaint_updates(models.Model): 
    complaint = models.ForeignKey(complaints,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    comment =models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    commented_by=models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.complaint)

    class Meta:
        verbose_name_plural="6.Complaint Updates"


class fir_details(models.Model):
    complaint = models.OneToOneField(complaints,on_delete=models.PROTECT)
    fir_number = models.CharField(max_length=225,unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.complaint)

    class Meta:
        verbose_name_plural="7.Fir Status"


class fir_status_report(models.Model): 
    fir = models.ForeignKey(fir_details,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    current_status =models.CharField(max_length=225)
 

    def __str__(self):
        return str(self.fir)

    class Meta:
        verbose_name_plural="8.Fir Status Report"
    


class news_feed(models.Model):
    date = models.DateTimeField(auto_now=True) 
    news = models.TextField()

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural="9.News Feed"

