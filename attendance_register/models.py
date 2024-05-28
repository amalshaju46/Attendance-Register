from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    present = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.student.name
    






