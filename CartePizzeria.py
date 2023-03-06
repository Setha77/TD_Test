class CartePizzeria:
    
    def __init__(self):
        self.carte = {}
        
    def is_empty(self):
        if(len(self.carte) == 0):
            return True
        return False
        
    def nb_pizzas(self):
        return len(self.carte)
    
    def add_pizza(self, pizza):
        self.carte[len(self.carte)] = pizza
        
    def remove_pizza(self, name):