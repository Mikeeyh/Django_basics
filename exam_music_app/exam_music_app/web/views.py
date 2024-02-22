from django.shortcuts import render, redirect

from exam_music_app.albums.models import Album
from exam_music_app.profiles.models import Profile
from exam_music_app.web.forms import CreateProfileForm

""" 
We create get_profile function in order to check if there is a profile created.
We need this verification for index view.
We gave the function Profile.objects.first() to check if there is any profile or not.
"""


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("index")  # upon clicking, redirects to the same page

    context = {
        "form": form,
        "no_navigation": True,  # Adding this to be able to remove navigation if no profile exists
    }
    return render(request, 'web/home-no-profile.html', context)


def index(request):
    profile = get_profile()

    if profile is None:
        return create_profile(request)

    context = {
        "albums": Album.objects.all(),  # taking the existing albums of the profile
    }

    return render(request, 'web/home-with-profile.html', context)


""" CBV EXAMPLE """
# class Index(views.TemplateView):
#     def get_template_names(self):
#         if get_profile() is None:
#             return ['web/home-no-profile.html']
#         return ['web/home-with-profile.html']
