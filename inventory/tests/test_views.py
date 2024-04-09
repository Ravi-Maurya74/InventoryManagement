from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from inventory.models import Inventory
import json


class TestViews(APITestCase):
    def setUp(self) -> None:
        self.listCreateUrl = reverse("list-create-inventory")

    def testInventoryCreateView(self):
        data = {
            "primary_location": "TestLocation",
            "vin": "VIN",
            "year": 2022,
            "cost": 150000.05,
            "selling_price": 100000.00,
        }
        response = self.client.post(self.listCreateUrl, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inventory.objects.count(), 1)
        self.assertEqual(Inventory.objects.get().primary_location, "TestLocation")

    def testInventoryListView(self):
        dataList = [
            {
                "primary_location": "TestLocation1",
                "vin": "VIN1",
                "year": 2022,
                "cost": 150000.05,
                "selling_price": 100000.00,
            },
            {
                "primary_location": "TestLocation2",
                "vin": "VIN2",
                "year": 2022,
                "cost": 150000.05,
                "selling_price": 100000.00,
            },
        ]

        for data in dataList:
            Inventory.objects.create(**data)

        response = self.client.get(
            self.listCreateUrl,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
