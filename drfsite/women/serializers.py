# import io
from rest_framework import serializers

from .models import Women

# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer


class WomenModel:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        # fields = ('title', 'content', 'cat')
        fields = "__all__"


# def encode():
#     model = WomenModel('Angelina Jolie', 'Content about Angelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#     return json


# def decode():
#     stream = io.BytesIO(encode())
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
