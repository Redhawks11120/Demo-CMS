import logging

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employees
from .serializers import EmployeesSerializer, DepartmentsSerializer


# Create your views here.

@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentsSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentsID=department_data['DepartmentsID'])
        department_serializer = DepartmentsSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentsID=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def employeeAPI(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeesSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeesSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == "PUT":
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeesID=employees_data['EmployeesID'])
        if employees_data['EmployeesName'] != "":
            employees_data['EmployeesName'] = employees_data['EmployeesName']
        else:
            employees_data['EmployeesName'] = employees.EmployeesName
        if employees_data['Department'] != "":
            employees_data['Department'] = employees_data['Department']
        else:
            employees_data['Department'] = employees.Department
        if employees_data['DateOfJoining'] != "":
            employees_data['DateOfJoining'] = employees_data['DateOfJoining']
        else:
            employees_data['DateOfJoining'] = employees.DateOfJoining
        employees_serializer = EmployeesSerializer(employees, data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        employees = Employees.objects.get(EmployeesID=id)
        employees.delete()
        return JsonResponse("Deleted Successfully", safe=False)
