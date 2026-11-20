"""TEAM AND PC STORAGE, based on how it works in pokemon games"""

MAX_TEAM_SIZE = 6    #you can only carry 6 pokemon at a time
MAX_PC_SIZE = 30   #One pc page holds 30

class Storage:
    def __init__(self):
        self.team = [] #list of pokemon on team, starts empty
        self.pc = []  #list of pokemon in pc, starts empty

    def add_pokemon(self, pokemon):
        if len(self.team) < MAX_TEAM_SIZE:   #if the team has room
            self.team.append(pokemon)   #add pokemon to team
            return "team"  #tell caller where it went
        if len(self.pc) < MAX_PC_SIZE:   #if team is full
            self.pc.append(pokemon)  #add to pc instead
            return "PC"
        raise ValueError("Storage is full") #both are full, report error

    def deposit(self, name):
        #todo support multiple PC boxes
        found = None  #will hold matching pokemon until we find it
        for p in self.team: #Look through the team
            if p.display_name() == name or p . species == name:  #match my nickname or species name of the pokemon
                found = p    #remember match
                break  #stop seatching
        if found is None: #nothing matches
            raise ValueError("Pokemon not found")    
        if len(self.team) == 1:    #its the only pokemon on your team left
            raise ValueError("You cannot deposit your last team member")
        if len(self.pc) >= MAX_PC_SIZE:  #no more room in the pc
            raise ValueError("PC is full")
        self.team.remove(found) #take off team
        self.pc.append(found) #put in pc
        return found #return the pokemon that was moved

    def withdraw(self, name):
        found = None
        for p in self.pc:
            if p.display_name() == name or p.species == name: #match by nickname or name of pokemon species
                found = p  #remember match
                break
        if found is None:
            raise ValueError("Pokemon not found")  
        if len(self.team) >= MAX_TEAM_SIZE: #team already has 6
            raise ValueError("Team is Full")
        self.pc.remove(found) #take it out of pc
        self.team.append(found) #add to the team
        return found

    def release(self, name):  
        for p in self.pc:   #Look in the pc
            if p.display_name() == name or p.species == name: #found the one we want to releast
                self.pc.remove(p) #remove it for good
                return p #return released pokemon
        raise ValueError("Pokemon not found")

    def team_average_level(self):
        total = 0
        for p in self.team: #go through each team member
            total += p.level   #add level
        return total / len(self.team)  #average = total / number of team members

    def team_summary(self):
        lines = [] #one text line per team member
        strongest = None #placeholder that will be filled with the strongest member
        for p in self.team: #go through teach team member
            lines.append(p.display_name() + " - Lv. " + str(p.level) + " " + "/".join(p.types) + " [" + p.level_label() + "]")  #An example (pikachu - Lv 12 Electric [Rookie])
        return lines

    def pc_summary(self):
        lines =[]  #one text line per pc pokemon
        for p in self.pc:    #go through each pokemon in the pc
            lines.append(p.display_name() + " - Lv. " + str(p.level) + " " + "/".join(p.types) + " [" + p.level_label() + "]")   # same format as the team summary
        return lines

