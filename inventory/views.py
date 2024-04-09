from django.shortcuts import render
from rest_framework import generics
from inventory.models import Inventory
from inventory.serializers import InventorySerializer

# Create your views here.


class ListCreateInventoryView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class RetrieveUpdateDestroyInventoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
