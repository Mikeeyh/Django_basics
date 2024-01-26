from django.shortcuts import render, redirect

from form_basics.web.forms import EmployeeForm, EmployeeModelForm
from form_basics.web.models import Employee


def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'GET':
        form = EmployeeModelForm(instance=employee)
    else:
        form = EmployeeModelForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('index-models')

    context = {
        "form": form,
        "employee":  employee,
    }

    return render(request, "web/employee_details.html", context)


def index_models(request):
    form = EmployeeModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index-models')

    context = {
        "employee_form": form,

        # To show all Employees:
        "employee_list": Employee.objects.all(),
    }

    return render(request, "web/modelform_index.html", context)

# SIMPLIFIED FULL CODE:


def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            print(form.cleaned_data)
            # use the data
            # redirect to some URL
            return redirect('index')

    context = {'employee_form': form}

    return render(request, 'web/index.html', context)


# FULL CODE:
#
# def index(request):
#     if request.method == 'GET':
#         context = {
#             "employee_form": EmployeeForm(),
#         }
#
#         return render(request, "web/index.html", context)
#
#     else:  # request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         print(request.POST['first_name'])
#
#         if form.is_valid():
#             # data is valid, populate 'cleaned_data'
#             print(form.cleaned_data['first_name'])  # prints the correct data after validation
#             # use the data
#             # redirect to some URL
#             return redirect('index')
#
#         else:  # data is INVALID, populate 'cleaned_data'
#             context = {
#                 "employee_form": form,
#             }
#
#             return render(request, "web/index.html", context)


# NOT GOOD EXAMPLE
# def index(request):
#     context = {
#         "employee_form": EmployeeForm(),
#     }
#
#     # print(request.GET)
#     print(request.POST['first_name']) # NOT CORRECT BECAUSE WE SKIP THE VALIDATION FROM forms.py
#
#     return render(request, "web/index.html", context)
