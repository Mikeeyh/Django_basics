from django.forms import modelform_factory
from django.urls import reverse_lazy
from django.views import generic as views

from exam_music_app.albums.models import Album
from exam_music_app.profiles.models import Profile

# TODO: Extract into a different module


def get_profile():  # Taking the Profile
    return Profile.objects.first()


class AlbumFormViewMixin:  # FOR PLACEHOLDERS
    def get_form(self, form_class=None):  # overwriting get_form method which returns our form
        form = super().get_form(form_class=form_class)

        # Can be moved a mixin
        form.fields['name'].widget.attrs["placeholder"] = "Album name"  # adding placeholder
        form.fields['artist_name'].widget.attrs["placeholder"] = "Artist name"
        form.fields['description'].widget.attrs["placeholder"] = "Description"
        form.fields['image_url'].widget.attrs["placeholder"] = "Image URL"
        form.fields['price'].widget.attrs["placeholder"] = "Price"

        return form


class ReadonlyAlbumFormViewMixin:  # FOR READONLY
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        for field_name, field in form.fields.items():
            field.widget.attrs['readonly'] = True

        return form

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #
    #     for field in form.fields.values():
    #         field.widget.attrs['readonly'] = "readonly"
    #
    #     return form


class CreateAlbumView(AlbumFormViewMixin, views.CreateView):
    queryset = Album.objects.all()  # model = Album
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    template_name = 'albums/album-add.html'
    success_url = reverse_lazy('index')

    """
    We cannot create an Album because we do not give the profile and we have this ERROR:
        IntegrityError at /album/add/
        NOT NULL constraint failed: albums_album.owner_id
    
    So we need to create get_profile() in order to take the Profile:
        def get_profile():
            return Profile.objects.first()
            
    Then we add form_valid() in order to add the instance profile
    """

    # If we DO NOT use a MIXIN we can just add it here:
    # def get_form(self, form_class=None):  # overwriting get_form method which returns our form
    #     form = super().get_form(form_class=form_class)
    #
    #     # Can be moved a mixin
    #     form.fields['name'].widget.attrs["placeholder"] = "Album name"  # adding placeholder
    #     form.fields['artist_name'].widget.attrs["placeholder"] = "Artist name"
    #     form.fields['description'].widget.attrs["placeholder"] = "Description"
    #     form.fields['image_url'].widget.attrs["placeholder"] = "Image URL"
    #     form.fields['price'].widget.attrs["placeholder"] = "Price"
    #
    #     return form

    def form_valid(self, form):  # saving it in advance. We write form_valid because we need to take the the profile
        # TODO: Check for a better solution
        form.instance.owner_id = get_profile().pk  # 1 line instead of the 2 lines above

        # instance = form.save(commit=False)  # commit=False will not send it to our DB
        # instance.owner = get_profile()  # we give the profile to our instance 'owner' from the model.py

        return super().form_valid(form)  # return redirect


class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = "albums/album-details.html"


class EditAlbumView(AlbumFormViewMixin, views.UpdateView):
    queryset = Album.objects.all()
    template_name = "albums/album-edit.html"
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    success_url = reverse_lazy('index')


class DeleteAlbumView(ReadonlyAlbumFormViewMixin, views.DeleteView):
    queryset = Album.objects.all()
    template_name = "albums/album-delete.html"
    success_url = reverse_lazy('index')

    # Creating a form using model_factory because the 'delete_view' does not return a form:
    form_class = modelform_factory(
        Album,
        fields=('name', 'artist_name', 'genre', 'description', 'image_url', 'price'),
    )

    """
    Overwriting get_form_kwargs() method 
    To show all information (data) 
    """
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs
