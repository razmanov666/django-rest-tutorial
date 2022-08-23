# from django.shortcuts import render
# from logging import exception
# from django.forms import model_to_dict
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import generics
from rest_framework import viewsets

from .models import Women
from .serializers import WomenSerializer


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
