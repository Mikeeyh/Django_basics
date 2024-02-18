from django.urls import path

from class_based_views_advanced.web.views import CreateTodoView, ListTodoView, DetailTodoVIew

urlpatterns = (

    # Normal view path:
    # path("create/", create_todo),

    path("", ListTodoView.as_view(), name="todos-list"),

    # Class based view path:
    path("create/", CreateTodoView.as_view(), name="todos-create"),

    # using pk
    path("<int:pk>/", DetailTodoVIew.as_view(), name="todos-detail"),

    # using slug
    path("<slug:slug>/", DetailTodoVIew.as_view(), name="todos-detail"),

    # using pk and slug
    path("<int:pk>/<slug:slug>/", DetailTodoVIew.as_view(), name="todos-detail"),
)
