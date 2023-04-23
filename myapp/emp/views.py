from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp
# Create your views here.
def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home.html", {'emps': emps})
    # return render(request, 'emp/home.html', {})

def add_emp(request):
    if request.method == 'POST':
        
        # data fetch
        emp_name = request.POST["emp_name"]
        emp_id   = request.POST["emp_id"]
        emp_phone = request.POST["emp_phone"]
        emp_address = request.POST["emp_address"]
        emp_work = request.POST.get('emp_work')
        emp_dept = request.POST["emp_dept"]

        #create model obj and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept
        if emp_work: e.working = True
        else: e.working = False

        #valide data  - skipped 

        #save the object
        e.save()
        
        
        return redirect("/emp/home/")
    return render(request, 'emp/add_emp.html', {})


def del_emp(request, emp_id):
    emp = Emp.objects.filter(emp_id=emp_id)
    emp.delete()
    return redirect("/emp/home/")


def update_emp(request, emp_id):
    emp = Emp.objects.get(emp_id=emp_id)
    return render(request, 'emp/update_emp.html', {'emp':emp})

def do_update(request, emp_id):
    if request.method == 'POST':
        
        # data fetch
        emp_name = request.POST["emp_name"]
        emp_id_temp   = request.POST["emp_id"]
        emp_phone = request.POST["emp_phone"]
        emp_address = request.POST["emp_address"]
        emp_work = request.POST.get('emp_work')
        emp_dept = request.POST["emp_dept"]

        #update model obj
        e = Emp.objects.get(emp_id=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept
        if emp_work: e.working = True
        else: e.working = False

        #save the object
        e.save()
        
    return redirect("/emp/home/")
    # return render(request, 'emp/update_emp.html', {})
