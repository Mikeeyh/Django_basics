from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Adding our app`s paths:
    path("", include('exam_music_app.web.urls')),
    path("album/", include('exam_music_app.albums.urls')),
    path("", include('exam_music_app.profiles.urls')),
]
