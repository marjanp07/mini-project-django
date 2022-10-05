from django.contrib import admin

# Register your models here.
from .models import *


class police_staff_inline(admin.TabularInline):
    model=police_staff
    extra=2


admin.site.register(User)

@admin.register(police_station)
class policeAdmin(admin.ModelAdmin):
    list_display=['name','place','district','phone_number']
    search_fields=["name","place",'phone_number']
    list_filter=["district"]
    inlines=[police_staff_inline]

@admin.register(police_staff)
class staffAdmin(admin.ModelAdmin):
    list_display=['police_station','user','person_name','place','state','district','post','phone_number','photo']


@admin.register(peoples)
class peoplesAdmin(admin.ModelAdmin):
    list_display=['user','person_name','place','state','district','post','adhar_number','phone_number','photo','police_station_range']

@admin.register(complaints)
class complaintsAdmin(admin.ModelAdmin):
    list_display=['user','police_station','complaint_discription','document_feild','date']

@admin.register(complaint_updates)
class cupdatesAdmin(admin.ModelAdmin):
    list_display=['complaint','date','comment','commented_by']


@admin.register(fir_details)
class fir_detailsAdmin(admin.ModelAdmin):
    list_display=['complaint','fir_number','date']

@admin.register(fir_status_report)
class fir_status_reportAdmin(admin.ModelAdmin):
    list_display=['fir','date','current_status']

@admin.register(news_feed)
class news_feedAdmin(admin.ModelAdmin):
    list_display=['date','news']
