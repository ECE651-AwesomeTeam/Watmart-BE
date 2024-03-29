"""watmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from backbone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signup),
    path('login', views.login),
    path('post', views.create_post),
    path('post/<product_id>', views.update_post),
    re_path(r'^mypost/$', views.get_my_post),
    path('order', views.create_order),
    path('order/<order_id>', views.update_order),
    re_path(r'^myorder/$', views.get_my_order),
    re_path(r'^post/$', views.get_post),
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT})
]
