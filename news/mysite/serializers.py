from rest_framework import serializers
from .models import Employees, Departments


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields =('DepartmentsID', 'DepartmentsName')

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields =('EmployeesID', 'EmployeesName', 'Department', 'DateOfJoining')