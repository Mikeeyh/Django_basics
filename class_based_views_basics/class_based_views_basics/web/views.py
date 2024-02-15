from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.shortcuts import render

from class_based_views_basics.web.models import Todo


def perform_always():
    pass


class BaseView(views.View):
    def dispatch(self, request, *args, **kwargs):
        perform_always()

        return super().dispatch(request, *args, **kwargs)


def index(request):  # Normal view
    perform_always()

    if request.method == 'POST':
        # perform post logic
        pass
    else:
        # perform get logic
        pass

    # Do some business logic

    return render(request, "web/index.html")


class IndexRawView(views.View):  # Class based view

    def dispatch(self, request, *args, **kwargs):
        # check permissions of user
        # if random() < 0.5:
        #     return HttpResponseNotAllowed(["get"])

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # perform get logic
        return render(request, "web/index.html")

    def post(self, request):
        # perform post logic
        pass


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = "web/details_todo.html"


class TodoListView(views.ListView):
    model = Todo
    template_name = "web/list_todos.html"

    def get_queryset(self):  # example search
        return super().get_queryset().filter(date__lte=datetime.now())


class TodoCreateView(views.CreateView):
    model = Todo
    fields = "__all__"
    template_name = "web/create_todo.html"

    # static way
    # success_url = reverse_lazy("index")

    # dynamic way
    def get_success_url(self):  # to show the created task after clicking on create button
        return reverse("todo_details", kwargs={"pk": self.object.pk})

    # Static way
    # form_class = TodoBaseForm

    # Dynamic way
    def get_form_class(self):
        # return TodoBaseForm
        return super().get_form_class()

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["deadline"].widget.attrs["type"] = "date"
        form.fields["deadline"].widget.attrs["class"] = "form-control"

        return form

    def form_valid(self, form):
        # Additional validation
        return super().form_valid(form)

    # Customization
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["todo_list"] = Todo.objects.all()  # to show created tasks in our create task page

        return context


class IndexView(views.TemplateView):
    # static templates
    template_name = "web/index.html"

    # dynamic templates
    # def get_template_names(self):

    # 'context' with static data, i.e. no DB calls
    extra_context = {
        "title": "With extra content",
        "static_time": datetime.now()
    }

    # 'context' with dynamic data, i.e. DB calls
    def get_context_data(self, **kwargs):  # overwriting the method
        context = super().get_context_data(**kwargs)

        context["dynamic_time"] = datetime.now()

        context["todo_list"] = Todo.objects.all()

        return context
