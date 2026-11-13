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

def languages():
    y=input("What language?, 语言?,言語?,click anything to continue,click X to leave")
    print("English")
    print("Chinese")
    print("Japanese")
    print("French")
    language_choice=input("Enter Character").strip()
    for i in range(1):
        if y==("x").lower():
            print("have a good day")
            break

    languages = {
        "1":"english",
        "2":"chinese",
        "3":"Japnese",
        "4":"French"
    }
    language=languages.get(language_choice)

    print(f' Using {language}')
languages()

    

