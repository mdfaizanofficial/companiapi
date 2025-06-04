from django.shortcuts import render
from rest_framework import viewsets, decorators, response
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    @decorators.action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)

        emps = Employee.objects.filter(company = company)

        emps_serializer = EmployeeSerializer(emps, many=True, context= {'request': request})

        return response.Response(emps_serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset =  Employee.objects.all()
    serializer_class = EmployeeSerializer