from django.urls import path, reverse

from urls_and_views_demos.departments.views import department_details, department_details_by_name

urlpatterns = (
    # path("", index),
    # path("index/", index),  # same as path("", index)

    # using regular method
    # path("departments/1/", department_1_details),
    # path("departments/2/", department_2_details),

    # using dynamic method '< >' (pk -> prime key)
    path("<int:pk>/", department_details, name="department_details"),
    path("<str:name>/", department_details_by_name),
)
