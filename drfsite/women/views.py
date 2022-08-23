from rest_framework import viewsets

from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
