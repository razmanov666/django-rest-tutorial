# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Women
from .permissions import IsAdminOrReadOnly
from .serializers import WomenSerializer

# from rest_framework.authentication import TokenAuthentication

# from .models import Category


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")

#         if not pk:
#             return Women.objects.all()

#         return Women.objects.filter(pk=pk)
#     @action(methods=["get"], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({"cats": cats.title})
