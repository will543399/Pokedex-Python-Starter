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
        language_choice = input("Enter a language: 1) English, 2) Chinese, 3) Japanese, or 4) French: ").strip().lower()
            language=languages.get((language_choice).lower())
            if language_choice in languages:
                lang=languages[language_choice]
                print(language_choice)
            elif language_choice in languages.value():
                    lang=langauge_choice
                    print(language_choice)
            else:
                print("invalid")
        search=input("Search your desired pokemon right now")
        matches[]
        length_search=len(search)
        name=pokemon["name"][language_choice]
        name_start=name[len(length_search)].lower
        if name_start==length_search:
                matches.append(name)

            
            
            
        
pokedexx()


    

