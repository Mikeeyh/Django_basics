from django import forms

from world_of_speed_app.profiles.models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }
