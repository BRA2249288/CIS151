introText = """You have entered a dark room. There is a light switch by the door,
a table in the center of the room, and two other doors to the left and right."""

def startAdv():
    print(introText)
    chooseText = input("Please type one option: left, right, table, or light: ")

    if chooseText == "left":
        print("you walk over to the left door")
        leftDoor()
    elif chooseText == "right":
        print("you walk over to the right door")
        rightDoor()
    elif chooseText == "table":
        inspectTable()
    elif chooseText == "light":
        lightSwitch()
    else:
        print("that isn't an option, silly!")
        startAdv()

def leftDoor():
    print("you open the door to the left, and you enter the parlor")
    prarlor()

def rightDoor():
    print("you open the door to the right, and...")

def lightSwitch():
    print("you turn on the light switch, and...")

def inspectTable():
    print("you approach the table, and discover...")

def parlor():
    print("You've entered the parlor. There is a bar on the south wall, there is a sofa on the right, and the card table in the center of the room")
    parlorChoice = input("Please choose one option: goto bar, sofa, or card table")
    if parlor Choice == "goto bar":
        print ("The ghost of harvey the bartender appears and pulls you into the portal")
        startAdv()
    elif parlorChoice == "sofa":
        print ("the floor beneath the sofa collapses, you fall into the basement")
        startAdv()
    elif parlorChoice == "card table":
        print ("the ghost of dealer invites you to play. Pull up a chair")
        #cardTable()
    

#def cardTable():

    
startAdv()
