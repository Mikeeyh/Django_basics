from django import forms

from exam_music_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):  # If no profile created, the home page displays a form for profile creation
    class Meta:
        model = Profile
        fields = ("username", "email", "age")

        # Adding placeholders:
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email",
                },
            ),
            "age": forms.NumberInput(
                attrs={
                    "placeholder": "Age",
                },
            ),
        }