from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^department$', views.departmentAPI),
    url(r'^department/([0-9]+)$', views.departmentAPI),
    url(r'^employee$', views.employeeAPI),
    url(r'^employee/([0-9]+)$', views.employeeAPI),
]