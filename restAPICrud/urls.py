from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createEmployeeRecord/',views.createEmployeeRecord),
    path('getEmployeeRecord/',views.getEmployeeRecord),
    path('getSingleEmployeeRecord/<str:email>/',views.getSingleEmployeeRecord),
    path('searchEmployeeRecord/',views.searchEmployeeRecord),
    path('deleteEmployeeRecord/<str:email>/',views.deleteEmployeeRecord),
    path('updateEmployeeRecord/',views.updateEmployeeRecord),
]



