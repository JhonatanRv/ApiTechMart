from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailProduto.as_view()),
    path('', ListProduto.as_view()),
    path('create', CreateProduto.as_view()),
    path('delete/<int:pk>', DeleteProduto.as_view())

]
