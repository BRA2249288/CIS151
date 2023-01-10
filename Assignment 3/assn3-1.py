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
    You're Spice! A rescue dog that Roommates aka Parents are going out of town.
    You plan on having a party. You have to figure out what you want to do first?
    """
    print(start_text)
    global choice
    select = input("Choose 's' for sock or 'd' for door: ")
    if select == "s":
        choice = "sock1"
    elif select == "d":
        choice = "godoor"
    else:
        print("That was not a valid choice")
        gamestart()
"""
    get sock:   Still on owner, get tossed in cage, start over
    """
def getsock(whichsock):
    sock1 = """
    Get Sock:
    You race for the sock and grab onto it with glee. Whoops, your owner
    is still wearing it. Back to the cage you go.
    """

    if whichsock == "sock1":
        print(sock1)
        global lifenumber
        lifenumber -= 1
        print("You only have %d lives left!" % lifenumber)
        gamestart()
    else:
        print("You got another sock!")
        global sockcount
        sockcount += 1
        print("You have %d socks" % sockcount)
        #set choice global and give it some value here

""" partly open door to hallway
    escape into hallway  choices
    down hallway   or go right
    """
def hallway():
    hallway_text = """
    Hallway:
    You squeeze out the door to the hallway. It's rather smooth tile
    so you tend to slide around a bit as you run. You can continue
    down the hallway or turn to your right.
    """
    print(hallway_text)
    global choice
    select = input(" 'h' for Down Hallway, or 'r' for right: ")
    if select == "h":
        choice = "togarage"
    elif select == "r":
        choice =  "tobathroom"
    else:
        print("That is not a valid choice")
        hallway()
        
    
"""
    go right :  Find bathroom
    choices:  steal toilet paper     or  hole in wall behind sink cabinet
    """

"""
    downhallway: Find workshop
    choices:  Attack snake   or  go under workbench
    """


"""
    Main Game Loop
    """
keepgoing = True
totallives = 5
lifenumber = 5
choice = "start"
sockcount = 0

while keepgoing:
    print("You chose:", choice)
    if lifenumber > 0 :
        if choice == "start":
            gamestart()
        elif choice == "sock1":
            getsock("sock1")
        elif choice == "godoor":
            hallway()
    else:
         print("Sorry, Ferrets don't have 9 lives, only 5.")
         keepgoing = False
    

