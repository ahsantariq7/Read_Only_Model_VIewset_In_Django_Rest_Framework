from django.urls import path,include
from model_viewset import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi', views.Model_viewset,basename='student')

urlpatterns = [
    path('model/',include(router.urls)),
]