from django.shortcuts import render,redirect
from Admin.models import *

# Create your views here.


def District(request):
    districts=tbl_districts.objects.all()
    if request.method=="POST":
        District=request.POST.get('txtdist')
        tbl_districts.objects.create(
            districts_name=District
        )
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'districts':districts})

def Adminreg(request):
    adminreg=tbl_adminreg.objects.all()
    if request.method=="POST":
        Adminregname=request.POST.get('txtname')
        Adminregemail=request.POST.get('txtemail')
        Adminregpassword=request.POST.get('txtpwd')
        tbl_adminreg.objects.create(
            admin_name= Adminregname,
            admin_email=Adminregemail,
            admin_password=Adminregpassword
        )
        return redirect('Admin/Adminreg')
    else:
        return render(request,'Admin/Adminreg.html',{'adminreg',adminreg})


def Type(request):
    Type=tbl_type.objects.all()
    if request.method=="POST":
        typename=request.POST.get('txttype')
        tbl_type.objects.create(
            type_name=typename
        )
        return redirect('Admin:Type')
    else:
        return render(request,'Admin/Type.html',{'type':Type})


def deltype(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect('Admin:Type')

def deldistrict(request,id):
    tbl_districts.objects.get(id=id).delete()
    return redirect('Admin:District')

def editdistrict(request,id):
    dis=tbl_districts.objects.get(id=id)
    if request.method=="POST":
        dis.districts_name=request.POST.get('txtdist')
        dis.save()
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'edit':dis})
    
def edittype(request,id):
    tip=tbl_type.objects.get(id=id)
    if request.method=="POST":
        tip.type_name=request.POST.get('txttype')
        tip.save()
        return redirect('Admin:Type')
    else:
        return render(request,'Admin/Type.html',{'edit':tip})


def place(request):
    dis=tbl_districts.objects.all()
    plc=tbl_place.objects.all()
    if request.method=="POST":
        place=request.POST.get('txtplace')
        district=request.POST.get('seldistrict')
        tbl_place.objects.create(
            place_name=place,
            district=tbl_districts.objects.get(id=district)

        )
        return redirect('Admin:place')
    else:
        return render(request,'Admin/Place.html',{'district':dis,'place':plc})

def delplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect('Admin:place')

def editplace(request,id):
    plc=tbl_place.objects.get(id=id)
    dis=tbl_districts.objects.all()
    if request.method=="POST":
        plc.place_name=request.POST.get('txtplace')
        plc.district=tbl_districts.objects.get(id=request.POST.get('seldistrict'))
        plc.save()
        return redirect('Admin:place')
    else:
        return render(request,'Admin/Place.html',{'edit':plc,'district':dis})