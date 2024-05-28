from datetime import date
from django.shortcuts import redirect, render



# # Create your views here.
from attendance_register.models import Attendance,Student


def index(request):
    return redirect('attendance')

def attendance(request):
    attendance = Attendance.objects.all()
    students = Student.objects.all()
    return render(request,"attendance.html",{'attendance':attendance,'students':students})

def attendance_create(request):
    if request.method == "POST":
        roll_no = request.POST.get('roll_no')
        student=Student.objects.get(roll_no=roll_no)
        attendance = Attendance(
            date = request.POST.get('date'),
            present = request.POST.get('present')=='True',
            student = student 
           
        )
        attendance.save()
    return redirect('attendance')

def submit_attendance(request):
    if request.method == "POST":
        students = Student.objects.all()

        for student in students:
            present = request.POST.get(str(student.roll_no)+'-present') == 'True'
            update = request.POST.get(str(student.roll_no)+'-update') == 'True'
            
            try:
                attendance_submitted = Attendance.objects.get(student=student,date=date.today())
            except Attendance.DoesNotExist:
                attendance_submitted = None
            
            if attendance_submitted != None:
                attendance_submitted.present = present
                if update:
                    attendance_submitted.save()
                continue
            
            attendance = Attendance(
                date = date.today(),
                present = present,
                student = student 
            )
            attendance.save()
    return redirect('attendance')


def student(request):
    student = Student.objects.all()
    return render(request,"student.html",{'student':student})

def student_create(request):
    if request.method == "POST":
       
        student = Student(
            name = request.POST.get('name'),
            roll_no = request.POST.get('roll_no'),
            address = request.POST.get('address'),
            phone = request.POST.get('phone'),
            date_of_joining = request.POST.get('date_of_joining')

            )
        student.save()
    return redirect('student')


