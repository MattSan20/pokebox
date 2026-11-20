"""Pokemon model used by the pokebox storage system"""

VALID_TYPES = [   #each type in the game
    "Normal", "Fire", "Water", "Grass", "Electric", "Ice",
    "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
    "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy",
]


class Pokemon:
    def __init__(self, species, level, types, nickname=None): #runs when a new pokemon is being made
        if level < 1 or level > 100:  #realistic level cap
            raise ValueError("Level must be between 1 and 100") #Report an error
        for t in types:    #check types that the pokemon was given
            if t not in VALID_TYPES:  #if not a real type
                raise ValueError("Unknown type: " + t)  #report error, type does not exist
        self.species = species   #store the species
        self.level = level   #store the level
        self.types = types    #store the list of types
        self.nickname = nickname   #store the nickname

    def display_name(self):
        if self.nickname == None:  #if the pokemon has no name
            return self.species #show the species name
        return self.nickname + " (" + self.species + ")" #otherwise show the nickname of the mon

    def level_label(self): 
        if self.level >= 70: 
            return "Core piece"   #level 70 and up
        elif self.level >= 40:
            return "Veteran"  #level 40 and up
        elif self.level >= 40:
            return "Experienced"  #level 40 and up
        elif self.level >= 20:
            return "Intermediate"
        else:
            return "Rookie" #anything under 20



    def to_dict(self): #Building a dictionary so it can be saved as a JSON
        return{
            "species" : self.species,
            "level": self.level,
            "types": self.types,
            "nickname": self.nickname
        }