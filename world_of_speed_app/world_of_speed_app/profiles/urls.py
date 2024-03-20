from django.urls import path, include

from world_of_speed_app.profiles.views import DeleteProfileView, EditProfileView, DetailProfileView
from world_of_speed_app.web.views import CreateProfileView

# from world_of_speed_app.web.views import create_profile

urlpatterns = (
    # path("create/", create_profile, name="create_profile"),
    path("create/", CreateProfileView.as_view(), name="create_profile"),

    path(
        "<int:pk>/",
        include([
            path("details/", DetailProfileView.as_view(), name="details_profile"),
            path("edit/", EditProfileView.as_view(), name="edit_profile"),
            path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
        ])
    ),
)
