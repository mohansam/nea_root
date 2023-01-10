"""nea_site URL Configuration

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
from django.views.generic.base import TemplateView
from user_profiles.views import Register, ChangePasswordView,change_password_success
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('user_profiles/', include('user_profiles.urls')),
    path('', include('django.contrib.auth.urls')),
    path('academic/', include('academic.urls')),
    path('', include('cal.urls')),
    path('', views.homepage, name='homepage'),
    path('posts/', include('posts.urls')),
    path('', include('pages.urls')),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
      path('password-success/', change_password_success, name='password_success')
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

