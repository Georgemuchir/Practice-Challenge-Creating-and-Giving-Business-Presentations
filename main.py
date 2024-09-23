class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_info(self):
        return f"Product: {self.name}, Cost: {self.cost}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self):
        return sum(product.cost for product in self.products)


class Manufacturer:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

    def add_to_inventory(self, product):
        self.inventory.add_product(product)

    def total_inventory_value(self):
        return self.inventory.total_value()


# Running example
if __name__ == "__main__":
    manufacturer = Manufacturer("SteelCorp")

    product1 = Product("Steel Rod", 500)
    product2 = Product("Iron Sheet", 700)

    manufacturer.add_to_inventory(product1)
    manufacturer.add_to_inventory(product2)

    print(f"Manufacturer: {manufacturer.name}")
    print(f"Total Inventory Value: {manufacturer.total_inventory_value()}")  # Output: 1200
