from django.shortcuts import render

from forms_advanced.web.forms import PersonForm

pf = PersonForm()

pf.is_valid()



