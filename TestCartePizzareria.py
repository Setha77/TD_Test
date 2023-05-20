from mock import Mock
from CartePizzareria import CartePizzareria, CartePizzeriaException

# Test pour savoir si la carte est vide
def test_carte_pizzareria_is_empty():
    carteP = CartePizzareria()
    assert carteP.is_empty()

# Test pour savoir si la carte n'est pas vide
def test_carte_pizzareria_is_not_empty():
    pizza = Mock()
    carteP = CartePizzareria()
    carteP.listePizza = [pizza]
    assert not carteP.is_empty()

# Test pour savoir le nombre de pizza dans la carte
def test_carte_pizzareria_getNb():
    pizza = Mock()
    carteP = CartePizzareria()
    assert carteP.getNbPizza() == 0

    carteP.listePizza = [pizza]
    assert carteP.getNbPizza() == 1

# Test pour savoir si la pizza a été ajouté
def test_carte_pizzareria_add_Pizza():
    pizza = Mock()
    carteP = CartePizzareria()
    carteP.add_Pizza(pizza)
    assert carteP.listePizza == [pizza]

# Test pour savoir la pizza a été retiré
def test_carte_pizzareria_remove():
    pizza = Mock
    carteP = CartePizzareria()
    carteP.listePizza = [pizza]
    carteP.remove_Pizza(pizza)
    assert carteP.listePizza == []

# Test pour savoir si le retirement de la pizza a échoué
def test_carte_pizzareria_not_remove():
    pizza = Mock()
    pizza2 = Mock()
    carteP = CartePizzareria()
    carteP.listePizza = [pizza]
    try: 
        carteP.remove_Pizza(pizza2)
    except CartePizzeriaException:
        pass
    else:
        raise Exception("L'exception n'a pas été levé")
