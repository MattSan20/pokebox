import pytest                                               # needed for pytest.raises

from pokebox.models import Pokemon                          # the class we're testing


def test_create_pokemon():
    p = Pokemon("Pikachu", 12, ["Electric"])                # create a valid Pokemon species and level should be stored correctly
    assert p.species == "Pikachu"                           
    assert p.level == 12                                   


def test_invalid_level_rejected():
    with pytest.raises(ValueError):                         # creating this SHOULD raise an error because level 150 is over 100
        Pokemon("Pikachu", 150, ["Electric"])               


def test_invalid_type_rejected():
    with pytest.raises(ValueError):                         # this SHOULD raise an error  because "Lightning" isn't a real type
        Pokemon("Pikachu", 12, ["Lightning"])             


def test_display_name_with_nickname():
    p = Pokemon("Charmander", 8, ["Fire"], nickname="Blaze")   # a Pokemon with a nickname shows "Nickname (Species)"
    assert p.display_name() == "Blaze (Charmander)"             


def test_level_label_champion():
    assert Pokemon("Dragonite", 75, ["Dragon", "Flying"]).level_label() == "Core piece"   # level 75 is Champion