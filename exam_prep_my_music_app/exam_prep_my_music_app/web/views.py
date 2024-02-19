from django.shortcuts import render

from exam_prep_my_music_app.profiles.models import Profile


""" 
We create get_profile function in order to check if there is a profile created.
We need this verification for index view.
We gave the function Profile.objects.first() to check if there is any profile or not.
"""


def get_profile():
    return Profile.objects.first()


def create_profile(request):  # we can use this function or just return this in index view
    return render(request, 'web/home-no-profile.html')


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    return render(request, 'web/home-with-profile.html')
