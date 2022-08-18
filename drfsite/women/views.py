# from django.shortcuts import render
# from logging import exception
# from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer

# from rest_framework import generics
# from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        womens = Women.objects.all()
        return Response({"posts": WomenSerializer(womens, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # post_new = Women.objects.create(
        #     title=request.data["title"],
        #     content=request.data["content"],
        #     cat_id=request.data["cat_id"],
        # )

        serializer.save()
        return Response({"post": serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})

        try:
            instance = Women.objects.get(pk=pk)

        except ObjectDoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method put not allowed"})

        Women.objects.filter(pk=pk).delete()

        return Response({"post": "delete post " + str(pk)})
