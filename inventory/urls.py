from django.urls import path
from inventory import views
import uuid

urlpatterns = [
    path("", views.ListCreateInventoryView.as_view(), name="list-create-inventory"),
    path(
        "<uuid:pk>/",
        views.RetrieveUpdateDestroyInventoryView.as_view(),
        name="retrieve-update-destroy-inventory",
    ),
]
