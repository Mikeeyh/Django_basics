import random

from django.shortcuts import render

cat_images = (
    'https://th.bing.com/th/id/R.41ec5c9ca2e897c49a0ab68e333da8e8?rik=dsYPYiGysjyoNA&riu=http%3a%2f%2fthewowstyle.com%2fwp-content%2fuploads%2f2015%2f04%2fcat1.jpg&ehk=GTCh9L6QOJd5t7FK13U8fi4c4z%2bqjD05seLLFGiHa1g%3d&risl=&pid=ImgRaw&r=0',
    'https://th.bing.com/th/id/R.7ceb81f6b2c615743919109333a742d5?rik=4SXH%2bKdUQ%2fhIbQ&riu=http%3a%2f%2fimages2.fanpop.com%2fimage%2fphotos%2f9400000%2fFunny-Cats-cats-9473111-1600-1200.jpg&ehk=zpmRdnX5thsU88ZKDfowPaEEzpGU3oUdfHeu3d05ZNA%3d&risl=&pid=ImgRaw&r=0',
)

cat_names = (
    'Pepelyashka',
    'Gosho',
)


def index(request):
    index = random.randint(0, len(cat_names) - 1)
    # To give us index of each object, so we can take its photo and name
    context = {
        'cat_image': cat_images[index],
        'cat_name': cat_names[index],

        # for our custom filter example:
        'numbers': [x + 1 for x in range(-10, 10)],
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')


def show_bootstrap(request):  # example from bootstrap.com
    context = {
        'has_bootstrap': request.GET.get('has_bootstrap', False),
    }
    return render(request, 'web/bootstrap.html', context)
