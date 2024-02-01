from django import forms
from django.forms import modelform_factory

from forms_advanced.web.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


PersonForm2 = modelform_factory(Person, fields="__all__")
# We can create a class using 'modelform_factory'. It is the same thing.

        # labels = {
        #     'first_name': 'First name:',
        # }
        #
        # error_messages = {
        #     'first_name': {
        #         # 'required': 'Please, enter your name'
        #     }
        # }
