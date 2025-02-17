from product import *

class Productmenager:
    def __init__(self):
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
        print(f"Proizvod '{product.name}'dodat u listu")
        
    def display_all_products(self):
        if not self.products:
            print("nema dostupnih proizvoda")
        else:
            for product in self.products:
                product.info_product()
                
    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(total)
        