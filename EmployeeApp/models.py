from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length = 50)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length= 100)
    department_name = models.CharField(max_length= 100)
    date_of_join = models.DateField()
    PhotoFileName = models.CharField(max_length= 100)
