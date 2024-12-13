import pytest
from json_handler import add_superheroes, check_superheroes_age

def test_add_and_sort_superheroes():
    new_heroes = [
        {"name": "Spider-Man", "age": 25},
        {"name": "Iron Man", "age": 48}
    ]
    add_superheroes('SuperHero.json', new_heroes)

    result = check_superheroes_age('superhero_new.json')
    assert result is False, "Ожидалось, что не все супергерои старше 30 лет"