"""the_acce URL Configuration

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
from django.urls import include, path
from django.views import debug


handler404 = 'home.views.error_404'
handler500 = 'home.views.error_500'
handler403 = 'home.views.error_403'
handler400 = 'home.views.error_400'

urlpatterns = [
    # Default Django project homepage
    path("debug/", debug.default_urlconf),
    # Django admin site
    path("admin/", admin.site.urls),
    # Refers to object BASE_DIR / home/urls.py
    path('', include("home.urls")),
    path('home/', include("home.urls")),
    # Refers to object BASE_DIR / matters/urls.py
    path('matters/', include("matters.urls")),
    # Refers to object BASE_DIR / accounts/urls.py
    path('accounts/', include("accounts.urls")),
    # Refers to object BASE_DIR / negotiations/urls.py
    path('negotiations/', include("negotiations.urls")),
]