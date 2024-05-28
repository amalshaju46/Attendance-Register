from django.contrib import admin
from .models import Student,Attendance

class StudentAdmin (admin.ModelAdmin):
    list_display = ('name','roll_no','date_of_joining')

class AttendanceAdmin (admin.ModelAdmin):
    list_display = ('student','present','date')   

admin.site.register(Student,StudentAdmin)
admin.site.register(Attendance,AttendanceAdmin)

