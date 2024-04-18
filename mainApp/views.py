from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

#CRUD Operations 

#read
class ListProduto(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

#update 
class DetailProduto(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

#create 
class CreateProduto(generics.CreateAPIView):
    queryset = Produto.objects.all
    serializer_class = ProdutoSerializer

#delete
class DeleteProduto(generics.DestroyAPIView): 
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    