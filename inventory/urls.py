from django.urls import path
from inventory import views

urlpatterns = [
    path("", views.ListCreateInventoryView.as_view(), name="list-create-inventory"),
]
