from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from exam_music_app.profiles.models import Profile

"""
Overwriting 'get_profile' method to take the profile.
Otherwise, it will show us this error:
AttributeError at /details/
Generic detail view DetailProfileView must be called with either 
an object pk or a slug in the URLconf.
"""


def get_profile():
    return Profile.objects.first()


class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profiles/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
