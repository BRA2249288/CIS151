"""  assn3.py
     A Text based style adventure game
     You're a Rescue Dog Spice ready to have a party!
     """


"""
 Start Game:  Describe rules, escape from cage, present first choices
    get sock  or go for partly open door
"""
def gamestart():
    start_text = """
    You're Spice! A rescue dog that Roommates aka Parents are going out of town. You plan on having a party. You have to figure out what you want to do first?"""
    introText = """Spice’s Roommates aka Parents leave for the day. Spice needs dogs treats, brew, food and guests to throw a rager! """
    introChoice = """Do you go to the backyard? Do you go upstairs? Do you jump in the pool? Do you sleep on the sofa? Do you steal all the dog toys?
    Do you use the Roommate aka “Rent’s” cell phone? Do you get a tasty Dog Frozen treat? """
    print(start_text)
    print(introText)
    global choice
    select = input("Choose 'back' for Backyard or 'up' for Upstairs or 'jump' for Pool or 'sleep' for Sofa or 'toys' for Toys or 'cell' for CellPhone or 'treat' for Treat ")
    if select == "BACK":
        goToBackyard()
    elif select == "UP":
        goToUpstairs()
    elif select == "JUMP":
        goToPool()
    elif select == "SLEEP":
        goToSofa()
    elif select == "TOYS":
        goToDogToys()
    elif select == "CELL":
        goToCellPhone()
    elif select == "TREAT":
        goToTreats()
    else:
        print("That was not a valid choice")
        gamestart()


gamestart() 
