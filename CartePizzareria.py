class CartePizzeriaException(Exception):
    pass

class CartePizzareria:
    def __init__(self):
        self.listePizza = []

    def getNbPizza(self):
        return len(self.listePizza)
    
    def is_empty(self):
       return len(self.listePizza) == 0
    
    def add_Pizza(self, pizza):
        self.listePizza.append(pizza)
    
    def remove_Pizza(self, name):
        try:
            self.listePizza.remove(name)
        except ValueError:
            raise CartePizzeriaException(f"{name} n'a pas été trouvé")

    
