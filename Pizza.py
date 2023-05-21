class Pizza:
    def __init__(self, name, prix, description, ingredient,  base):
        self.name = name
        self.prix = prix
        self.base = base
        self.description = description
        self.listeIngredients = ingredient

class Boisson:
    def __init__(self, name, prix, alcool):
        self.name = name
        self.prix = prix
        self.alcool = alcool

class Dessert:
    def __init__(self, name, prix, ingredient, realisation):
        self.name = name
        self.prix = prix
        self.ingredient = ingredient
        self.realisation = realisation