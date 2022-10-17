from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import *
from .serializers import *


# class BookAPIList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookAPIUpdate(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Book.objects.all()[:3]
        return Book.objects.filter(pk=pk)

    @action(methods = ['get'], detail = True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
    # class BookAPIView(APIView):
    #     def get(self, request):
    #         w = Book.objects.all()
    #         return Response({'posts': BookSerializer(w, many=True).data})
    #
    #     def post(self, request):
    #         serializer = BookSerializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({'post': serializer.data})
    #
    #     def put(self, request, *args, **kwargs):
    #         pk = kwargs.get("pk", None)
    #         if not pk:
    #             return Response({"error": "Method PUT not allowed"})
    #         try:
    #             instance = Book.objects.get(pk=pk)
    #         except:
    #             return Response({"error": "Method PUT not allowed"})
    #
    #         serializer = BookSerializer(data=request.data, instance=instance)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({"post": serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method DELETE not allowed"})
    #     try:
    #         instance_del = Book.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Method DELETE not allowed"})
    #
    #     serializer = BookSerializer(data=request.data, instance=instance_del)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})
# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
