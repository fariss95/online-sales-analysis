from product import *
from product_menager import *


manager = Productmenager()

product1 = Product("Laptop", 80000, 5)
product2 = Product("Telefon", 50000, 10)
product3 = Product("Televizor", 70000, 3)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

manager.display_all_products()
manager.total_value()
