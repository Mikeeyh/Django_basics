from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import modelform_factory, modelformset_factory
from django.urls import reverse

from forms_advanced.web.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ('created_by',)

    # Adding the placeholder 'Enter your first name' in our PersonForm, adds it in our UpdatePersonForm too.
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))

    labels = {
        "first_name": "Enter first name:",
    }

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')  # for save example we should get out 'user' because there isn't any args/kwargs in ModelForm __init__
        super().__init__(*args, **kwargs)

        # for our crispy from example:
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("create-person")
        self.helper.add_input(Submit('submit', 'Create person'))

    def clean(self, *args, **kwargs):     # CLEAN: Checks the data using clean:
        cleaned_data = super().clean(*args, **kwargs)

        print(cleaned_data)
        return cleaned_data  # Return all data

    # def clean_first_name(self):  # Return the specified data (first_name)
    #     pass  # This give 'None' as value of our 'first_name'

    def save(self, commit=True):  # SAVE: Example of saving the user who added its names&age
        instance = super().save(commit=False)  # We get the 'instance' from 'cleaned_data'
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance


# ------------------------------------------------------------------------
# --------------------------------MIXIN-----------------------------------
# ------------------------------------------------------------------------

class ReadonlyFieldsMixin:
    readonly_fields = ()

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

        # for _, field in self.fields.items():  # '_,' means nothing, we should have it because 'fields' is a dictionary
        #     field.widget.attrs['readonly'] = 'readonly'


class BootstrapFormMixin:  # other example:
    def _init_bootstrap_form(self):
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------


class UpdatePersonForm(ReadonlyFieldsMixin, BootstrapFormMixin, PersonForm):
    # UpdatePersonForm(PersonForm) if we do not use mixin

    # using mixin:
    readonly_fields = ("age",)  # we add fields in which we do not want to be able to write

    # Adding the placeholder for 'age' does not affect 'age' of PersonForm class because of the inheritance
    age = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Age verified'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # this super().__init__ calls the __init__ of our PersonForm
        # the __init__ of the PersonForm will call the __init__ of ModelForm

        # using mixin
        self._mark_readonly_fields()
        self._init_bootstrap_form()

        # without mixin
        # self.fields["age"].widget.attrs["readonly"] = "readonly"


# We can create a class using 'modelform_factory':
PersonForm2 = modelform_factory(Person, fields="__all__")  # It is the same thing.

# FORMSET:
PersonFormSet = modelformset_factory(Person, exclude=('created_by',), extra=2, max_num=2)
# extra -> 2 forms / max_num -> 1 form shown only
