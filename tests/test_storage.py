import pytest  #needed for pytest.raises

from pokebox.models import Pokemon  #to create test pokemon
from pokebox.storage import Storage  #the class that we're testing

def make_pokemon(species="Spearow", level = 5):
    return Pokemon(species, level, ['Normal', "Flying"])  #simple test pokemon


def test_first_six_go_to_team():
    storage = Storage() #fresh, empty storage
    for i in range(6):  #add 6 pokemon
        assert storage.add_pokemon(make_pokemon()) == "team" #each one should go to the team
    assert len(storage.team) == 6 #team is now full

def test_seventh_pokemon_goes_to_pc():
    storage = Storage()
    for i in range(6):
        storage.add_pokemon(make_pokemon()) 
    assert storage.add_pokemon(make_pokemon("Pikachu")) == "PC"  #the 7th pokemon should go to the pc
    assert len(storage.pc) == 1  #pc now has 1


def test_deposit_moves_to_pc():
    storage = Storage()
    storage.add_pokemon(make_pokemon("Spearow"))  #team: Spearow
    storage.add_pokemon(make_pokemon("Weedle")) #team: Spearow, Weedle
    storage.deposit("Spearow") #only move spearow to pc
    assert len(storage.team) == 1 #only weedle should be left on the team
    assert storage.pc[0].species == "Spearow" #Spearow is now in the pc

def test_cannot_deposit_only_one_team_member():
    storage = Storage()
    storage.add_pokemon(make_pokemon())   #only 1 member in team
    with pytest.raises(ValueError):   #depositing it should fail
        storage.deposit("Spearow")

def test_team_average_level():
    storage = Storage()
    storage.add_pokemon(make_pokemon(level = 10) )#level 10
    storage.add_pokemon(make_pokemon(level = 20)) #level 20
    assert storage.team_average_level() == 15 #should be an average level of 15
