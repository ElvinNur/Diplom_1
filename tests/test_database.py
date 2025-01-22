import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_initialization():
    db = Database()

    assert len(db.buns) == 3
    assert len(db.ingredients) == 6

    assert db.buns[0].get_name() == "black bun"
    assert db.buns[0].get_price() == 100
    assert db.buns[1].get_name() == "white bun"
    assert db.buns[1].get_price() == 200
    assert db.buns[2].get_name() == "red bun"
    assert db.buns[2].get_price() == 300

    assert db.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert db.ingredients[0].get_name() == "hot sauce"
    assert db.ingredients[0].get_price() == 100

    assert db.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
    assert db.ingredients[3].get_name() == "cutlet"
    assert db.ingredients[3].get_price() == 100


def test_available_buns():
    db = Database()

    buns = db.available_buns()

    assert len(buns) == 3

    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[1].get_name() == "white bun"
    assert buns[1].get_price() == 200
    assert buns[2].get_name() == "red bun"
    assert buns[2].get_price() == 300


def test_available_ingredients():
    db = Database()

    ingredients = db.available_ingredients()

    assert len(ingredients) == 6

    assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[0].get_price() == 100

    assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[1].get_name() == "sour cream"
    assert ingredients[1].get_price() == 200

    assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredients[2].get_name() == "chili sauce"
    assert ingredients[2].get_price() == 300

    assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[3].get_price() == 100

    assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[4].get_name() == "dinosaur"
    assert ingredients[4].get_price() == 200

    assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
    assert ingredients[5].get_name() == "sausage"
    assert ingredients[5].get_price() == 300