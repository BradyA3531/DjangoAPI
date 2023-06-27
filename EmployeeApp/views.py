from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer


# Create your views here.

@csrf_exempt
def departmentApi(request, id = 0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_serialzer = DepartmentSerializer(department, many = True)
        return JsonResponse(department_serialzer.data, safe = False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serialzer = DepartmentSerializer(data = department_data)
        if department_serialzer.is_valid():
            department_serialzer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to Add", safe = False)
    
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Department.objects.get(department_id = department_data['department_id'])
        department_serialzer = DepartmentSerializer(department, data = department_data)
        if department_serialzer.is_valid():
            department_serialzer.save()
            return JsonResponse("Updated Succesfully", safe = False)
        return JsonResponse("Failed to update", safe = False)
    
    elif request.method == "DELETE":
        department = Department.objects.get(department_id = id)
        department.delete()
        return JsonResponse('Deleted succesfully', safe = False)
    

@csrf_exempt
def employeeApi(request, id = 0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serialzer = EmployeeSerializer(employee, many = True)
        return JsonResponse(employee_serialzer.data, safe = False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serialzer = EmployeeSerializer(data = employee_data)
        if employee_serialzer.is_valid():
            employee_serialzer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to Add", safe = False)
    
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employee_id = employee_data['employee_id'])
        employee_serialzer = EmployeeSerializer(employee, data = employee_data)
        if employee_serialzer.is_valid():
            employee_serialzer.save()
            return JsonResponse("Updated Succesfully", safe = False)
        return JsonResponse("Failed to update", safe = False)
    
    elif request.method == "DELETE":
        employee = Employee.objects.get(employee_id = id)
        employee.delete()
        return JsonResponse('Deleted succesfully', safe = False)