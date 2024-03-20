from django.forms import modelform_factory
from django.urls import reverse_lazy

from world_of_speed_app.cars.forms import CreateCarForm
from world_of_speed_app.cars.models import Car
from django.views import generic as views

from world_of_speed_app.profiles.models import Profile


def get_profile():  # Taking the Profile
    return Profile.objects.first()


class ReadonlyAlbumFormViewMixin:  # FOR READONLY
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for field_name, field in form.fields.items():
            field.widget.attrs['readonly'] = True

        return form


class CatalogueListView(views.ListView):
    model = Car
    template_name = 'cars/catalogue.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_cars'] = self.get_queryset().count()
        return context


class CreateCarView(views.CreateView):
    model = Car
    form_class = CreateCarForm
    template_name = 'cars/car-create.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


class CarDetailView(views.DetailView):
    queryset = Car.objects.all()
    template_name = "cars/car-details.html"


class CarEditView(views.UpdateView):
    queryset = Car.objects.all()
    template_name = "cars/car-edit.html"
    fields = ('type', 'model', 'year', 'image_url', 'price')
    success_url = reverse_lazy('catalogue')


class CarDeleteView(ReadonlyAlbumFormViewMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy('catalogue')

    form_class = modelform_factory(
        Car,
        fields=('type', 'model', 'year', 'image_url', 'price'),
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

