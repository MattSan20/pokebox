"""Command line interfact for pokebox"""

import argparse #pythons built in tool for command line arguements

from pokebox.models import Pokemon #this is for creating new pokemon
from pokebox.save_file import load, save #load or save trainers data

SAVE_PATH = "pokebox_save.json"   #the save file is created in the current folder

def main(argv=None):
    parser = argparse.ArgumentParser(description="PokeBox: manage your pokemon team and your pc") #setting up command parser
    parser.add_argument("command", choices=["add", "team", "pc", "deposit", "withdraw", "release"]) #the actions that you wilkl be able to do
    parser.add_argument("species", nargs="?") #the pokemons name
    parser.add_argument("--level", type=int, default = 5)  #level for "add column" defaults to level 5
    parser.add_argument("--types", default="Normal")   #types for add
    parser.add_argument("--nickname") #optional, nickname for pokemon
    args = parser.parse_args(argv) #read what the user has typed out

    storage = load(SAVE_PATH) #load saved team and pc

    if args.command == "add": #add a new pokemon
        if args.species:
            pokemon = Pokemon(args.species, args.level, args.types.split(","), args.nickname) #create the pokemon
            where = storage.add_pokemon(pokemon)  #goes to team or pc
            print(pokemon.display_name() + " was sent to your " + where) #tell the user where it went
        else:
            print("Please give a species name")
    elif args.command == "team": #show the team
        if len(storage.team) == 0: #Print teach team member's line
            print("Your team is empty") 
        else:
            for line in storage.team_summary(): #print the each pokemon team meber's line
                print(line)
            print("Average level: " + str(round(storage.team_average_level(), 1))) #print the teams average level
    elif args.command == "pc": #now we show the pc
        if len(storage.pc) == 0:
            print("Pc is Currently Empty")
        else:
            for line in storage.pc_summary():  #print each PC pokemon's line
                print(line)
    elif args.command == "deposit":  #move a team member to the pc
        if args.species:
            try:
                p = storage.deposit(args.species) #try to deposit the pokemon
                print(p.display_name() + " was moved to the pc")
            except ValueError as e: #Pokemon not found
                print(e) #show an error message instead of crashing
        else:
            print("Please give a species name") 
    elif args.command == "withdraw": #move a pokemon from your pc to the real team
        if args.species:
            try:
                p = storage.withdraw(args.species) #Try to withfraw the pokemon
                print(p.display_name() +" was added to the team" )
            except ValueError as e:
                print(e)
        else:
            print("Please give a species name")
    elif args.command == "release": #release the pokemon from the pc
        if args.species:
            try:
                p = storage.release(args.species) #try to release the pokemon
                print(p.display_name() + " was released forever. Goodbye :( )")
            except ValueError as e:
                print(e)
        else:
            print("Please give a species name")

    save(storage, SAVE_PATH)  #save all the changes so they're there for us next time

if __name__ == "__main__": #this only runs if the file is run directly
    main()