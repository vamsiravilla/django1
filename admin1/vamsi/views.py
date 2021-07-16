from django.shortcuts import render
from vamsi.models import *
# Create your views here.
def sai(request):
    data=student.objects.all()
    return render(request,'home.html',{'data':data})
def salman(request):
    data1=employee.objects.all()
    return render(request,'emp.html',{'data1':data1})
def satya(request):
    data2=HR.objects.all()
    return render(request,'HR.html',{'data2':data2})