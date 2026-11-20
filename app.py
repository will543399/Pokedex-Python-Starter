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
        "3":"japanese",
        "4":"french"
    }
#def get_choice(z):
#    while True:
#   user_input=input("pokemon you're looking for")
#       if user_input=0:
#           print("try again")
#        else:
#           matches={item for item in z if }
#def showitems():
#    language_item=input("Enter Character").strip()
#    language=languages.get(language_)
#    if not language:
#        print("invalid")

def pokedexx():
    choice = input("Enter a language: 1) English, 2) Chinese, 3) Japanese, or 4) French: ").strip().lower()
    language=languages.get((choice).lower())
    if choice in languages:
        lang=languages[choice]
        print(choice)
    elif choice in languages.values():
        lang=choice
        print(choice)
    else:
        print("invalid")
    if choice=="1":
        search=str(input("Search your desired pokemon right now").lower())
    elif choice=="2":
        search2=str(input("搜索宝可梦"))
    elif choice=="3":
        search3=input("ポケモンを探す")
    elif choice=="4":
        search4=input("Recherche un Pokémon")
        search4==search2
        search3==search4
    while True:
        if choice=="1":
            search=str(input("Search your desired pokemon right now").lower())
        elif choice=="2":
            search2=str(input("搜索宝可梦").lower())
        elif choice=="3":
            search3=str(input("ポケモンを探す").lower())
        elif choice=="4":
            search4=str(input("Recherche un Pokémon").lower())
        matches=[]
        length_search=len(search)
        for item in data:
            pokemon=search(item['name'])
            print(pokemon)
        language=language.get(choice,"english")
        pokemon_data=pokemon
        name=pokemon_data["name"](choice)
        name_start=name[len(length_search)].lower()
        if name_start==length_search:
            matches.append(name)
matches=[]
'''    if choice=="1":
        search=str(input("Search your desired pokemon right now").lower())
        length_search=len(search)
        for item in data:
            pokemon=search(item['name'])
            print(pokemon)
        language=language.get(choice,"english")
        pokemon_data=pokemon
        name=pokemon_data["name"](choice)
        name_start=name[len(length_search)].lower()
        if name_start==length_search:
            matches.append(name)
        elif choice=="2":
            search2=str(input("搜索宝可梦").lower())
            length_search=len(search2)
            for item in data:
                pokemon=search(item['name'])
                print(pokemon)
            language=language.get(choice,"english")
            pokemon_data=pokemon
            name=pokemon_data["name"](choice)
            name_start=name[len(length_search)].lower()
            if name_start==length_search:
                matches.append(name)
        elif choice=="3":
            search3=str(input("ポケモンを探す").lower())
            length_search=len(search3)
            for item in data:
                pokemon=search(item['name'])
                print(pokemon)
            language=language.get(choice,"english")
            pokemon_data=pokemon
            name=pokemon_data["name"](choice)
            name_start=name[len(length_search)].lower()
            if name_start==length_search:
                matches.append(name)
        elif choice=="4":
            search4=str(input("Recherche un Pokémon").lower())
            length_search=len(search)
            for item in data:
                pokemon=search(item['name'])
                print(pokemon)
            language=language.get(choice,"english")
            pokemon_data=pokemon
            name=pokemon_data["name"](choice)
            name_start=name[len(length_search)].lower()
            if name_start==length_search:
                matches.append(name)'''

            
            
            
        
pokedexx()


    

