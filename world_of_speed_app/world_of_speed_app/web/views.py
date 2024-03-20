# from django.shortcuts import render, redirect
#
# from world_of_speed_app.profiles.forms import ProfileModelForm
# from world_of_speed_app.profiles.models import Profile
#
#
# def get_profile():
#     return Profile.objects.first()
#
#
# def create_profile(request):
#     form = ProfileModelForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect("index")  # upon clicking, redirects to the same page
#
#     context = {
#         "form": form,
#         "no_navigation": True,  # Hide navigation links on create profile page
#     }
#     return render(request, 'profiles/profile-create.html', context)
#
#
# def index(request):
#     profile = get_profile()
#
#     if profile is None:
#         context = {
#             "no_navigation": True,  # Hide navigation links on create profile page
#         }
#
#         return render(request, 'web/index.html', context)
#
#     # If a profile exists, render the index page
#     return render(request, 'web/index.html')

from django.shortcuts import render, redirect
from django.views import generic as views
from world_of_speed_app.profiles.forms import ProfileModelForm
from world_of_speed_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class IndexView(views.TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.first()
        context['no_navigation'] = profile is None
        return context


class CreateProfileView(views.CreateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'profiles/profile-create.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'no_navigation': True})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form, 'no_navigation': True})
