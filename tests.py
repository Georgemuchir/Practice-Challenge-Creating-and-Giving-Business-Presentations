import unittest
from main import Product, Inventory, Manufacturer

class TestProduct(unittest.TestCase):
    def test_product_info(self):
        product = Product("Steel Rod", 500)
        self.assertEqual(product.get_info(), "Product: Steel Rod, Cost: 500")


class TestInventory(unittest.TestCase):
    def test_inventory_value(self):
        inventory = Inventory()
        product1 = Product("Steel Rod", 500)
        product2 = Product("Iron Sheet", 700)
        inventory.add_product(product1)
        inventory.add_product(product2)
        self.assertEqual(inventory.total_value(), 1200)


class TestManufacturer(unittest.TestCase):
    def test_total_inventory_value(self):
        manufacturer = Manufacturer("SteelCorp")
        product1 = Product("Steel Rod", 500)
        product2 = Product("Iron Sheet", 700)
        manufacturer.add_to_inventory(product1)
        manufacturer.add_to_inventory(product2)
        self.assertEqual(manufacturer.total_inventory_value(), 1200)


if __name__ == "__main__":
    unittest.main()
