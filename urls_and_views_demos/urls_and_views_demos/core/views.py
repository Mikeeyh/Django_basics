import json

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index_no_template(request, *args, **kwargs):

    content = f"<h1>It works with:</h1><br/>" + \
              f"args={args} and kwargs={kwargs},<br/>" + \
              f"path={request.path},<br/>" + \
              f"method={request.method},<br/>" + \
              f"user={request.user}."

    return HttpResponse(content)

# This shows us in the browser:

# It works with:
#
# args=() and kwargs={},
# path=/,
# method=GET,
# user=mike.(because we created a superuser mike)


def index(request, *args, **kwargs):  # with template using render()
    context = {
        "title": "Requested data",
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": request.user,
    }

    return render(request, 'core/index.html', context)


# redirect is using for redirecting to some other path
def redirect_to_softuni(request):
    return redirect("https://softuni.bg")


def redirect_to_index(request):
    return redirect('index_no_params')


def redirect_to_index_with_params(request):
    return redirect('index_with_pk_and_slug', pk=19, slug="Mike")


def index_json(request, *args, **kwargs):
    content = {
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": str(request.user),
    }

    return JsonResponse(
        content,
        content_type="application/json",
    )

# This shows us in the browser:
# {
#     "args": "()",
#     "kwargs": "{'pk': 17, 'slug': 'mike'}",
#     "path": "/json/17/mike/",
#     "method": "GET",
#     "user": "mike"
# }


# Errors example


def raise_error(request):
    return HttpResponseNotFound()


def raise_exception(request):  # We should create Django Template otherwise the user will see some details of our code.
    raise Http404
