import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
languages = {
        "1":"english",
        "2":"chinese",
        "3":"japnese",
        "4":"french"
    }

#def showitems():
#    language_item=input("Enter Character").strip()
#    language=languages.get(language_)
#    if not language:
#        print("invalid")

def pokedexx():
choice = input("Enter a language: 1) English, 2) Chinese, 3) Japanese, or 4) French: ").strip().lower()
    language=languages.get((language_choice).lower())
    if not languages:
        print("invalid")
    else:
        print(language_choice)
    for pokemon in data:
        name=input("character name")
        
        print(pokemon["name"][language_choice])
        
    matches=[]

    print(f' Using {language}')
    for pokemon in data:
        if not isinstance(pokemon,dict):
            continue
        names=pokemon.get("name",{})
        if language_choice==1:
            name=names.get("English"," ")
        elif language_choice==2:
            name=names.get("Chinese"," ")
        elif language_choice==3:
            name=names.get("Japanese"," ")
        elif language_choice==4:
            name=names.get("French"," ")
        else:
            continue
        
pokedexx()


    

