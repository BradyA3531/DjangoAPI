from rest_framework import serializers
from EmployeeApp.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_id','department_name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'employee_name', 'department_name', 'date_of_join', 'PhotoFileName')