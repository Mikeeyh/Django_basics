import json
import random

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from class_based_views_advanced.web.models import Todo


@login_required
# -> decorator to enter only if logged in.
def index(request):  # for example
    context = {
        'todo_list': [t.title for t in Todo.objects.all()],
    }
    return HttpResponse(json.dumps(context))


class FilterTodoByTitleForm(forms.Form):
    title_pattern = forms.CharField(
        max_length=Todo.MAX_TITLE_LENGTH,
        required=False,
    )

    is_done = forms.BooleanField(
        required=False,
    )


class DetailTodoVIew(views.DetailView):
    model = Todo
    template_name = 'web/detail_todo.html'
    slug_field = 'slug'
    query_pk_and_slug = True

    def dispatch(self, request, *args, **kwargs):
        # To restrict the user to do not enter something we DO NOT want:
        # if request.user.tenant != request.GET.get('tenant'):
        #     raise
        return super().dispatch(request, *args, **kwargs)

    """ 
    This is to show how tenant filters our todo_list objects 
    (example URL: http://localhost:8000/8276/?tenant=softuni)
    We add 'tenant' in 'model.py' too
    And we add some tenant description in DB
    """
    def get_queryset(self):
        queryset = super().get_queryset()

        tenant = self.request.GET.get('tenant', None)
        if tenant is not None:
            queryset = queryset.filter(tenant=tenant)
        return queryset


"""
Example of MIXIN for our ListTodoView CBV -> show latest_created_count (objects)
We also should add our Mixin: class ListTodoView(LatestCreatedMixin, views.ListView)
"""


class LatestCreatedMixin:
    latest_created_count = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-pk')[:self.latest_created_count]


class ListTodoView(views.ListView):  # need 2 things to work:
    model = Todo
    template_name = 'web/todo_list.html'

    latest_created_count = 7

    # queryset = Todo.objects.all() == model = Todo
    # template_name = "web/todo_list.html" Is NOT NECESSARY to be added:
    # if the template name follows the pattern `{APP_NAME}/{MODEL_NAME}_list.html`
    # it is automatically found

    """
    Example of function paginate -> gives us only 'N' number results from our 'list'
    (We should remove paginate functionality to see the example of LatestCreatedMixin
    """

    # Static way:
    default_paginate_by = 5

    # Dynamic way:
    # def get_paginate_by(self, queryset=None):
    #     return random.randint(2, 5)

    """
    We can overwrite get_context_data:
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # taking initial context

        context["title"] = 'Todos list'  # adding title named 'Todos list'

        # For SEARCH BAR (adding initial does not clean the searched thing after clicking on 'Search' button
        context["filter_form"] = FilterTodoByTitleForm(
            initial={
                'title_pattern': self.get_title_pattern(),
            }
        )

        return context  # returns the new context, and we can go to our html and add it

    """
    We can overwrite get_paginate_by: 
    """
    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by', self.default_paginate_by)
        return paginate_by

    """
    We can overwrite get_queryset (if we used it instead of 'model = 'Todo'): 
    """
    def get_queryset(self):

        # taking the initial queryset
        queryset = super().get_queryset()

        queryset = self.apply_filter(queryset)

        return queryset

    def apply_filter(self, queryset):

        # For SEARCH BAR (DYNAMIC):
        title_pattern = self.get_title_pattern()
        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        # For is_done functionality:
        # is_done = self.get_is_done_filter()
        # if is_done is not None:
        #     queryset = queryset.filter(is_done=is_done)

        return queryset

    def get_is_done_filter(self):
        return self.request.GET.get('is_done', None) == 'on'

    def get_title_pattern(self):  # For SEARCH BAR
        return self.request.GET.get("title_pattern", None)


class CreateTodoView(views.CreateView):
    model = Todo  # or queryset [{'title': 'todos 1'}]

    fields = ('title', 'description')  # or 'exclude or form_class

    # Optional
    template_name = "web/create_todo.html"

    # Optional
    success_url = reverse_lazy('todos-list')  # for index example


"""
----CRUD-----
1. Create
    - CreateView
    
2. Read (details, list)
    - DetailView
    - LisView
    
3. Update
    - UpdateView
    
4. Delete
    - DeleteView
"""
