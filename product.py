class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def info_product(self):
        print(f"Product name: {self.name},product price: {self.price},product quantity: {self.quantity}")
        
    def update_quantity(self,new_quantity):
        if new_quantity >= 0:
            self.quantity =new_quantity
        else:
            print("Greska: Kolicina ne moze biti negativna.")
            
        