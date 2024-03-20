from django.db.models import Sum
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from world_of_speed_app.cars.models import Car
from world_of_speed_app.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


class DetailProfileView(views.DetailView):
    model = Profile
    template_name = 'profiles/profile-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        total_sum = Car.objects.filter(owner=profile, owner__isnull=False).aggregate(total_price=Sum('price'))['total_price'] or 0
        context['total_sum'] = total_sum
        return context

    def get_object(self, queryset=None):
        return get_profile()


class EditProfileView(views.UpdateView):
    template_name = "profiles/profile-edit.html"
    success_url = reverse_lazy("catalogue")

    form_class = modelform_factory(
        Profile,
        fields=('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture'),
    )

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()
