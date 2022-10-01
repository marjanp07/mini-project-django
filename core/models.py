from django.db import models

# Create your models here.

class police_station(models.Model):
    name = models.CharField(max_length=225)
    place = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    phone_number = models.IntegerField()


class peoples(models.Model):
    name = models.CharField(max_length=225)
    Place = models.CharField(max_length=225)
    nationality = models.CharField(max_length=225)
    district = models.CharField(max_length=225)
    post = models.CharField(max_length=225) 
    adhar_number = models.IntegerField()
    photo = models.ImageField(upload_to="people/")
    police_station_range= models.ForeignKey(police_station,on_delete=models.PROTECT)


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

 