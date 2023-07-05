from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employees

# Create your views here.
def emp_home(request):
    # return HttpResponse("<h1>Employees Home Page</h1>")
    emps = Employees.objects.all()
    return render(request, 'emp/home.html',{
        'emps' : emps
    })

def add_emp(request):
    if request.method == "POST":
        # data fatch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone  = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        #Validations 

        # create model object and set the data
        e = Employees()
        e.name = emp_name
        e.emp_id = emp_id
        e.phoneNo = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        #save the object
        e.save()
        #prepare massage
        return redirect("/emp/home/")    
    return render(request, 'emp/add_emp.html',{})

def delete_emp(request,emp_id):
    emp = Employees.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/emp/home/')

def update_emp(request,emp_id):
    emp = Employees.objects.get(pk=emp_id)
    return render(request, 'emp/update_emp.html', {
        'emp' : emp
    })

def do_update_emp(request,emp_id):
    if request.method == 'POST':
        # data fatch
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone  = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Employees.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phoneNo = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        #save the object
        e.save()
        #prepare massage
        return redirect('/emp/home/')
    



    


