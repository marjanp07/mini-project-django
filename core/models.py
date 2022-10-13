from operator import truediv
from secrets import choice
from tabnanny import verbose
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from versatileimagefield.fields import VersatileImageField,PPOIField
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural="1.App Users"

class states(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural="2.states"

class district(models.Model):
    state= models.ForeignKey(states,on_delete=models.PROTECT)
    name=models.CharField(max_length=225)

    def __str__(self):
        return str(self.name)
        
    class Meta:
        verbose_name_plural="3.districts"

    
class police_station(models.Model):
    name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    district = models.ForeignKey(district,on_delete=models.PROTECT)
    state = models.ForeignKey(states,on_delete=models.PROTECT)
    phone_number = models.IntegerField()

    def __str__(self):
        return str(self.name)


    class Meta:
        verbose_name_plural="4.Police station"


class police_staff(models.Model):
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    person_name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    state = models.ForeignKey(states,on_delete=models.PROTECT)
    district = models.ForeignKey(district,on_delete=models.PROTECT)
    post = models.CharField(max_length=225) 
    phone_number = models.IntegerField(unique=True)
    image_ppoi=PPOIField()
    photo = VersatileImageField(upload_to="police/",ppoi_field='image_ppoi')

    def __str__(self):
        return str(self.user)


    class Meta:
        verbose_name_plural="5.Police Staff"
    

class peoples(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT,null=True,blank=True)
    police_station_range= models.ForeignKey(police_station,on_delete=models.PROTECT)
    person_name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    state = models.ForeignKey(states,on_delete=models.PROTECT)
    district = models.ForeignKey(district,on_delete=models.PROTECT)
    post = models.CharField(max_length=225) 
    adhar_number = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True)
    image_ppoi=PPOIField('Image PPOI')
    photo = VersatileImageField(upload_to="people/",blank=True,null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural="6.Peoples"


class complaints(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    complaint_discription = models.CharField(max_length=225)
    document_feild = models.FileField(upload_to="complaints/")
    date = models.DateTimeField(auto_now=True)

    def get_latest_update(self):
        return complaint_updates.objects.filter(complaint=self).last()
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural="7.Complaints"



class complaint_updates(models.Model): 
    STATUS_CHOICE = (('OPEN','OPEN'),('PENDING','PENDING'),('FIR CREATED','FIR CREATED'),('COLSED','COLSED'))

    complaint = models.ForeignKey(complaints,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    comment =models.CharField(max_length=225)
    status=models.CharField(max_length=225,choices=STATUS_CHOICE)
    commented_by=models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.complaint)

    class Meta:
        verbose_name_plural="9.Complaint Updates"


class fir_details(models.Model):
    complaint = models.OneToOneField(complaints,on_delete=models.PROTECT)
    fir_number = models.CharField(max_length=225,unique=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.complaint)

    class Meta:
        verbose_name_plural="91.Fir Status"


class fir_status_report(models.Model): 
    fir = models.ForeignKey(fir_details,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    current_status =models.CharField(max_length=225)
 

    def __str__(self):
        return str(self.fir)

    class Meta:
        verbose_name_plural="92.Fir Status Report"
    


class news_feed(models.Model):
    date = models.DateTimeField() 
    heading =models.CharField(max_length=225)
    district = models.ForeignKey(district,on_delete=models.PROTECT)
    news = models.TextField()
    image_ppoi=PPOIField()
    photo = VersatileImageField(upload_to="news/",ppoi_field='image_ppoi')

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name_plural="93.News Feed"

