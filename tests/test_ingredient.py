import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize( 
    "ingredient_type, name, price",
    [
        ("filling", "Говяжий метеорит (отбивная)", 3000),
        ("sauce", "Соус Spicy-X", 90)
    ]
)

def test_ingredient(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    
    assert ingredient.get_type() == ingredient_type
    
    assert ingredient.get_name() == name
    
    assert ingredient.get_price() == price