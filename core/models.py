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

class police_station(models.Model):
    name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    phone_number = models.IntegerField()

class police_and_staff_mapping(models.Model):
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    user = models.OneToOneField(User,on_delete=models.PROTECT)

class peoples(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    person_name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    nationality = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    post = models.CharField(max_length=225) 
    adhar_number = models.IntegerField(unique=True)
    phone_number = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to="people/")
    police_station_range= models.OneToOneField(police_station,on_delete=models.PROTECT)


class complaints(models.Model):
    user = models.ForeignKey(peoples,on_delete=models.PROTECT)
    police_station = models.ForeignKey(police_station,on_delete=models.PROTECT)
    complaint_discription = models.CharField(max_length=225)
    document_feild = models.FileField(upload_to="complaints/")
    date = models.DateTimeField(auto_now=True)

class complaint_updates(models.Model): 
    complaint = models.ForeignKey(complaints,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    comment =models.CharField(max_length=225)
    commented_by=models.CharField(max_length=225)


class fir_details(models.Model):
    complaint = models.ForeignKey(complaints,on_delete=models.PROTECT)
    case_number = models.CharField(max_length=225,unique=True)
    date = models.DateTimeField(auto_now=True)


class fir_status_report(models.Model): 
    fir = models.ForeignKey(fir_details,on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    current_status =models.CharField(max_length=225)


class news_feed(models.Model):
    date = models.DateTimeField(auto_now=True) 
    news = models.TextField()

 