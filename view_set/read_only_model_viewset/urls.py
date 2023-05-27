from django.urls import path,include
from read_only_model_viewset import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi', views.Model_read_only_viewset,basename='student')

urlpatterns = [
    path('read/',include(router.urls)),
]