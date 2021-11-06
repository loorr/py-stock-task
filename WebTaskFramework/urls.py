"""WebTaskFramework URL Configuration

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
from django.urls import path
from django.conf.urls import url

from WebTaskFramework.controller import pageOne
from AkshareApp.controller import views as akshareViews
from WebTaskFramework.controller.docs import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', pageOne.hello, name='home'),
    url("akshare/", akshareViews.akshare_hello),
    url("get-stock-item", akshareViews.get_stock_item),
    url(r'^docs/$', schema_view, name="schema_view"),
]
