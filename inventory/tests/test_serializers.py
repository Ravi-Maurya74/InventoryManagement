from django.test import TestCase
from inventory.models import Inventory
from inventory.serializers import InventorySerializer


class TestSerializers(TestCase):
    def setUp(self):
        self.inventory_data = {
            "primary_location": "Location",
            "vin": "VIN",
            "year": 2022,
            "cost": 150000.05,
            "selling_price": 100000.00,
        }

        self.inventory = Inventory.objects.create(**self.inventory_data)
        self.serializer = InventorySerializer(instance=self.inventory)

    def testSerializerContainsExpectedFields(self):
        data = self.serializer.data
        expected_fields = [
            "sku",
            "primary_status",
            "primary_location",
            "vin",
            "make",
            "model",
            "year",
            "cost",
            "selling_price",
            "created_at",
            "last_updated_at",
        ]
        self.assertEqual(set(data.keys()), set(expected_fields))

    # def testSerializerDataMatchesInventoryData(self):
    #     data = self.serializer.data
    #     for key, value in self.inventory_data.items():
    #         self.assertEqual(data[key], value)

    def testValidDataDeserialization(self):
        valid_data = {
            "primary_location": "Location",
            "vin": "VIN",
            "year": 2022,
            "cost": 1000.00,
            "selling_price": 1500.00,
        }
        serializer = InventorySerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        inventory_instance = serializer.save()
        self.assertIsInstance(inventory_instance, Inventory)
        for key, value in valid_data.items():
            self.assertEqual(getattr(inventory_instance, key), value)

    def testInvalidDataDeserialization(self):
        invalid_data = {
            "vin": "VIN",
            "year": 2022,
            "cost": 1000.00,
            "selling_price": 1500.00,
        }
        serializer = InventorySerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("primary_location", serializer.errors)
