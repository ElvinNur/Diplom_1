import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize("ingredient_type", ["filling", "sauce"])
    def test_get_type(self, ingredient_type):
        """Проверяет, что метод get_type возвращает правильный тип ингредиента."""
        ingredient = Ingredient(ingredient_type, "Тестовый ингредиент", 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["Говяжий метеорит (отбивная)", "Соус Spicy-X"])
    def test_get_name(self, name):
        """Проверяет, что метод get_name возвращает правильное имя ингредиента."""
        ingredient = Ingredient("filling", name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [3000, 90])
    def test_get_price(self, price):
        """Проверяет, что метод get_price возвращает правильную цену ингредиента."""
        ingredient = Ingredient("filling", "Тестовый ингредиент", price)
        assert ingredient.get_price() == price
