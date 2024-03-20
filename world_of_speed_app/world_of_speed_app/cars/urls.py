from django.urls import path, include

from world_of_speed_app.cars.views import CatalogueListView, CreateCarView, CarDetailView, CarEditView, CarDeleteView


urlpatterns = (
    path('catalogue/', CatalogueListView.as_view(), name='catalogue'),
    path('create/', CreateCarView.as_view(), name='car_create'),

    path(
        "<int:pk>/",
        include([
            path("details/", CarDetailView.as_view(), name="details_car"),
            path("edit/", CarEditView.as_view(), name="edit_car"),
            path("delete/", CarDeleteView.as_view(), name="delete_car"),
        ])
    ),
)
