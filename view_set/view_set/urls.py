"""view_set URL Configuration

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
from django.urls import path,include
from view import views
from model_viewset import views
from read_only_model_viewset import views
#from rest_framework.routers import DefaultRouter

#router=DefaultRouter()
#router1=DefaultRouter()

#router.register('studentapi', views.Student_viewset,basename='student')
#router1.register('student', views.Model_viewset,basename='model')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include(router.urls)),
    #path('api/',include(router1.urls)),
    path('',include('view.urls')),
    path('',include('model_viewset.urls')),
    path('',include('read_only_model_viewset.urls')),
]
