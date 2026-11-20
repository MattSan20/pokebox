from pokebox.models import Pokemon #creating and testing pokemon
from pokebox.save_file import load, save
from pokebox.storage import Storage #to create storage to save

def test_save_and_load(tmp_path): #temporary folder for pytest
    storage = Storage()
    storage.add_pokemon(Pokemon("Psyduck", 9, ["Water"], nickname="Headache"))
    path = tmp_path / "save.json" #save file inside the temporary folder
    save(storage, path) #save it
    loaded = load(path) #load it back
    assert loaded.team[0].display_name() =="Headache (Psyduck)" #the same pokemon thatcame back

def test_missing_file_gives_empty_storage(tmp_path):
    loaded = load(tmp_path / "does_not_exist.json") #try to load file that does not exist