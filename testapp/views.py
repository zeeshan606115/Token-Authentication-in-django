from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,\
IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from testapp.permissions import IsReadOnly, namePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from testapp.authentications import CustomAuthentication


# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   # authentication_classes = [JSONWebTokenAuthentication, ]
    authentication_classes = [CustomAuthentication, ]
   # permission_classes=[JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]