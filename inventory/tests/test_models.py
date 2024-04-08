from django.test import TestCase
from inventory.models import Inventory


class TestModels(TestCase):

    def setUp(self) -> None:
        self.inventory = Inventory.objects.create(
            primary_location="Location",
            vin="VIN",
            year=2023,
            cost=1100000,
            selling_price=700000,
        )
        self.inventory2 = Inventory.objects.create(
            primary_location="Location2",
            vin="VIN2",
            year=2023,
            cost=900000,
            selling_price=500000,
        )

    def testDefaultPrimaryStatusValue(self):
        self.assertEqual(self.inventory.primary_status, "CREATED")

    def testDefaultDateValue(self):
        self.assertIsNotNone(self.inventory.created_at)
        self.assertIsNotNone(self.inventory.last_updated_at)

    def testSkuGeneration(self):
        self.assertIsNotNone(self.inventory.sku)

        self.assertNotEqual(self.inventory.sku, self.inventory2.sku)
