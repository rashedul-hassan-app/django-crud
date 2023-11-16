from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

# List all employees


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee/employee_list.html', context)
