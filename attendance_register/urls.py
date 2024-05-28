from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('attendance/',views.attendance,name='attendance'),
    path('student/',views.student,name='student'),
    path('attendance/create/',views.attendance_create,name='attendance_create'),
    path('student/create/',views.student_create,name='student_create'),
    path('attendance/submit-attendance/',views.submit_attendance,name='submit_attendance')
]