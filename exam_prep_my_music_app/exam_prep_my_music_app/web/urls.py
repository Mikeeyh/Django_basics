from django.urls import path

from exam_prep_my_music_app.web.views import index

urlpatterns = (
    path("", index, name="index"),
)
