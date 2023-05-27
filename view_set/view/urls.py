from django.urls import path,include
from view import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi', views.Student_viewset,basename='student')

urlpatterns = [
    path('api/',include(router.urls)),
]