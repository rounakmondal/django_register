from operator import concat
from unicodedata import name
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,"app/index.html")

def insertdata(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    phone=request.POST['phone']
    contact=request.POST['contact']

    newuser=students.objects.create(FirstName=fname,LasttName=lname,email=email,Contact=contact,phone=phone)
    alldata=students.objects.all()
    return render(request,"app/show.html",{"key1":alldata})


def contactme(request):
    return render(request,"app/insertdata.html")

def conta(request):
    name=request.POST['name']
    email=request.POST['email']
    message=request.POST['message']
    newcontact=contactmee.objects.create(Name=name,EmailField=email,Message=message)
    return redirect('index')


def editdata(request,pk):
    user_data=students.objects.get(id=pk)
    return render(request,"app/editform.html",{"editdata":user_data})


def updatebaby(request):


    id=request.POST['id']
    # id=17
    user_update=students.objects.get(id=id)
    user_update.FirstName=request.POST['fname']
    user_update.LasttName=request.POST['lname']
    user_update.email=request.POST['email']
    user_update.phone=request.POST['phone']
    user_update.Contact=request.POST['contact']
    user_update.save()
    return redirect('index')

def deldata(request,dele):
    del_data=students.objects.get(id=dele)
    del_data.delete()
    alldata=students.objects.all()
    return render(request,"app/show.html",{"key1":alldata})

def register(request):
    return render(request,"app/register.html")
