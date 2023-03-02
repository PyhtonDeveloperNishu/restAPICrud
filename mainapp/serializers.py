from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=50)
    phone = serializers.CharField(max_length=15)
    dsg = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)

    def create(self,validatedData):
        return Employee.objects.create(**validatedData)


    def update(self,instance,validatedData):
        if("name" in validatedData and validatedData['name']!=''):
            instance.name = validatedData['name']
        if("email" in validatedData and validatedData['email']!=''):
            instance.email = validatedData['email']
        if("phone" in validatedData and validatedData['phone']!=''):
            instance.phone = validatedData['phone']
        if("dsg" in validatedData and validatedData['dsg']!=''):
            instance.dsg = validatedData['dsg']
        if("salary" in validatedData and validatedData['salary']!=''):
            instance.salary = validatedData['salary']
        if("city" in validatedData and validatedData['city']!=''):
            instance.city = validatedData['city']
        if("state" in validatedData and validatedData['state']!=''):
            instance.state = validatedData['state']
        instance.save()
        return instance