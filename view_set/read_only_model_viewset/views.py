from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


class Model_read_only_viewset(viewsets.ReadOnlyModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer