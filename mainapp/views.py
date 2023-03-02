from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import io

from .models import Employee
from .serializers import EmployeeSerializer
@csrf_exempt
def createEmployeeRecord(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    empSerializer = EmployeeSerializer(data=pythonData)
    if(empSerializer.is_valid()):
        empSerializer.save()
        msg = {"result":"Done","msg":"Record is Created!!!"}
    else:
        msg = {"result":"Fail","msg":"Record is Invalid or Email Already Exist!!!"}

    # e = Employee()
    # e.name = pythonData['name']
    # e.email = pythonData['email']
    # e.phone = pythonData['phone']
    # e.dsg = pythonData['dsg']
    # e.salary = pythonData['salary']
    # e.city = pythonData['city']
    # e.state = pythonData['state']
    # e.save()

    responseMessage = JSONRenderer().render(msg)
    return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def getEmployeeRecord(Request):
    data = Employee.objects.all()
    dataSerializer = EmployeeSerializer(data,many=True)
    jsonData = JSONRenderer().render(dataSerializer.data)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def getSingleEmployeeRecord(Request,email):
    try:
        data = Employee.objects.get(email=email)
        dataSerializer = EmployeeSerializer(data,many=False)
        jsonData = JSONRenderer().render(dataSerializer.data)
        return HttpResponse(jsonData,content_type="application/json")
    except:
        msg = {"result":"Fail","msg":"Record Not Found"}
        jsonData = JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")
@csrf_exempt
def updateEmployeeRecord(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    try:
        emp = Employee.objects.get(email=pythonData['email'])
        employeeSerializer = EmployeeSerializer(emp,data=pythonData,partial=True)
        if(employeeSerializer.is_valid()):
            employeeSerializer.save()
            msg = {"result":"Done","msg":"Record is Upated!!!"}            
        else:   
            msg = {"result":"Fail","msg":"Record is Not Valid!!!"}            
    except:
        msg = {"result":"Fail","msg":"Record Not Fond!!!"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def deleteEmployeeRecord(Request,email):
    try:
        data = Employee.objects.get(email=email)
        data.delete()
        msg = {"result":"Fail","msg":"Record Is Deleted"}
    except:
        msg = {"result":"Fail","msg":"Record Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def searchEmployeeRecord(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    search = pythonData['search']
    data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(city__icontains=search)|Q(state__icontains=search)|Q(dsg__icontains=search))
    dataSerializer = EmployeeSerializer(data,many=True)
    jsonData = JSONRenderer().render(dataSerializer.data)
    return HttpResponse(jsonData,content_type="application/json")
















# from django.shortcuts import render,HttpResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# import io

# from .models import Employee

# @csrf_exempt
# def createEmployeeRecord(Request):
#     jsonData = Request.body
#     stream = io.BytesIO(jsonData)
#     pythonData = JSONParser().parse(stream)

#     e = Employee()
#     e.name = pythonData['name']
#     e.email = pythonData['email']
#     e.phone = pythonData['phone']
#     e.dsg = pythonData['dsg']
#     e.salary = pythonData['salary']
#     e.city = pythonData['city']
#     e.state = pythonData['state']
#     e.save()

#     data = {"result":"Done","msg":"Record is Created!!!"}
#     responseMessage = JSONRenderer().render(data)
#     return HttpResponse(responseMessage,content_type="application/json")




# @csrf_exempt
# def getEmployeeRecord(Request):
#     pass

# @csrf_exempt
# def getSingleEmployeeRecord(Request):
#     pass

# @csrf_exempt
# def upateEmployeeRecord(Request):
#     pass

# @csrf_exempt
# def deleteEmployeeRecord(Request):
#     pass

# @csrf_exempt
# def searchEmployeeRecord(Request):
#     pass


























# @csrf_exempt
# def getEmployeeRecord(Request):
#     data = [
#         {"id":1001,"name":"Nitin Chauhan","dsg":"Trainer"},
#         {"id":1002,"name":"Nitin Chauhan","dsg":"Trainer"},
#         {"id":1003,"name":"Nitin Chauhan","dsg":"Trainer"},
#         {"id":1004,"name":"Nitin Chauhan","dsg":"Trainer"},
#         {"id":1005,"name":"Nitin Chauhan","dsg":"Trainer"},
#         {"id":1006,"name":"Nitin Chauhan","dsg":"Trainer"}
#     ]
#     jsonData = JSONRenderer().render(data)
#     return HttpResponse(jsonData,content_type="application/json")
