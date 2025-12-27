import uuid

class Product:

    cals_kj = 4.184
    def __init__(self, name, price_per_kg, calories):
        self.name = name
        self.price_per_kg = price_per_kg
        self.calories = calories

    def kilo_joules(self):
        return self.calories * Product.cals_kj
    @staticmethod
    def generate_id():
        return f"Product-{uuid.uuid4().hex}"
    
    
        


banana = Product("Banana", 1.2, 89)
tomato = Product("tomato", 1.0, 70)

print(tomato.kilo_joules())
print(tomato.calories)

bid = Product.generate_id()
print(bid)