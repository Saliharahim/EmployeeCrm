from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Employee
from api.serialilzers import EmployeeSerializer


# Create your views here.


class EmployeeView(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    model=Employee
