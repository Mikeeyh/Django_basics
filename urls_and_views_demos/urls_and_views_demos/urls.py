"""urls_and_views_demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('urls_and_views_demos.core.urls')),

    path("departments/", include('urls_and_views_demos.departments.urls')),

]


"""
Difference between 'path' and 'str' in urls:
|                         | departments/<str:name>/ | departments/<str:name>/<str:fname>/ | departments/<path:name>/ |
| departments/gosho/pesho | No match                | Match: name=gosho, fname=pesho      | Match: gosho/pesho       |
"""


"""
When creating new Django App:
1. Add the Django App in 'INSTALLED_APPS'
2. Create 'urls.py' in the Django App
3. Include the Django App's 'urls.py' in global 'urls.py'
"""