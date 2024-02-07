from django.http import HttpResponse
from django.shortcuts import render

from forms_advanced.web.forms import PersonForm, UpdatePersonForm, PersonFormSet
from forms_advanced.web.models import Person


def index(request):
    person_form = PersonForm()
    update_person_form = UpdatePersonForm()

    context = {
        "person_form": person_form,
        "update_person_form": update_person_form,

        "person_list": Person.objects.all(),
    }

    return render(request, "web/index.html", context)


def create_person(request):
    form = PersonForm(request.POST, request.FILES, user=request.user)
    # we add 'user=request.user' for our save method example in forms.py

    if form.is_valid():
        form.save()
    # return HttpResponse("Form submission successful!")


def show_formset(request):
    form_set = PersonFormSet()
    context = {
        "form_set": form_set,
    }

    return render(request, "web/formsets.html", context)
