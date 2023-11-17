from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# List all employees


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee/employee_list.html', context)


def employee_add_or_update(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee/employee_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            print(employee.name)
            print(employee.id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()

        return redirect('/employee/list')
