from django import forms

from form_basics.web.models import Employee


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=True,
        help_text="Enter your first name",
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name"})
    )

    email = forms.EmailField(
        help_text="Enter your email address"
    )

    age = forms.IntegerField(
        help_text="Enter your age"
    )

    INTERESTS = (
            (1, "Gaming"),
            (2, "Education"),
            (3, "Watching"),
            (4, "Sport"),
    )

    interests = forms.ChoiceField(
        choices=INTERESTS,
        required=False,
    )

    interests2 = forms.IntegerField(
        widget=forms.Select(choices=INTERESTS),
        required=False,
    )

    interests3 = forms.CharField(
        widget=forms.RadioSelect(choices=INTERESTS),
        required=False,
    )

    interests4 = forms.CharField(
        widget=forms.CheckboxSelectMultiple(choices=INTERESTS),
        required=False,
        help_text="Choose your interest"
    )

    password = forms.IntegerField(
        widget=forms.PasswordInput(),
        help_text="Enter your password"
    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=(
            ("male", "Male"),
            ("female", "Female"),
        ),
        help_text="Choose your gender"
    )


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        # WE HAVE ALSO:

        # exclude = ('role')
        # help_texts
        # labels
        # error_messages

        widgets = {
            'role': forms.RadioSelect,
        }

        # widgets = {
        #     'role': forms.RadioSelect(
        #         attrs={
        #             'disabled': 'disabled',
        #         }
        #     ),
        # }

# NORMAL FORM WITHOUT A MODEL:--------------------------------------------------------------

# class EmployeeNormalForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=Employee.MAX_FIRST_NAME_LENGTH,
#         required=True,
#     )
#
#     last_name = forms.CharField(
#         max_length=35,
#         required=True,
#     )
#
#     role = forms.IntegerField(
#         widget=forms.RadioSelect(choices=Employee.ROLES),
#         required=True,
#     )
