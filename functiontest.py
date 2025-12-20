class Product:
    def __init__(self, name, price_per_kg, calories):
        self.name = name
        self.price_per_kg = price_per_kg
        self.calories = calories

    def do_something(self):
        print(f"this is a {self.name}")
        pass


banana = Product("Banana", 1.2, 89)
tomato = Product("tomato", 1.0, 40)


print(tomato.calories)
banana.do_something()