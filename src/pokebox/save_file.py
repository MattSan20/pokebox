"""Saves and loads the trainer's storage to a JSON file."""   # docstring describing this file

import json                                                   # Python's built-in tool for reading/writing JSON

from pokebox.models import Pokemon                            # needed to rebuild Pokemon objects when loading
from pokebox.storage import Storage                           # needed to create the storage object


def save(storage, path):
    data = {                                                  # put everything into one dictionary
        "team": [p.to_dict() for p in storage.team],          # convert each team Pokemon to a dictionary
        "pc": [p.to_dict() for p in storage.pc],              # convert each PC Pokemon to a dictionary
    }
    with open(path, "w") as f:                                # open the file for writing ("w")
        json.dump(data, f, indent=2)                          # write the data as nicely formatted JSON


def load(path):
    try:
        with open(path) as f:                                 # open the save file for reading
            data = json.load(f)                               # read the JSON back into a dictionary
    except:                                                   # if anything goes wrong while opening/reading...
        return Storage()                                      # ...start with empty storage
    storage = Storage()                                       # create a fresh storage object
    for d in data["team"]:                                    # rebuild each team Pokemon from its dictionary
        storage.team.append(Pokemon(d["species"], d["level"], d["types"], d["nickname"]))
    for d in data["pc"]:                                      # rebuild each PC Pokemon from its dictionary
        storage.pc.append(Pokemon(d["species"], d["level"], d["types"], d["nickname"]))
    return storage                                            # hand back the loaded storage