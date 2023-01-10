##Intro Text 
introText = """You have entered Game On. Your mission is to find Metal Jesus. You can go straight,
You can go back or you can go Left or Right."""
##Start Game Function
def startAdv():
    print(introText)
    chooseText = input("Please type one option: left, right, straight, or back: ")
    if chooseText.upper() == "LEFT":
        print("you walk over to the left door")
        leftRoute()
    elif chooseText.upper() == "RIGHT":
        print("you walk over to the right door")
        rightRoute()
    elif chooseText.upper() == "STRAIGHT":
        straightRoute()
    elif chooseText.upper() == "BACK":
        backRoute()
    else:
        print("that isn't an option, silly!")
        startAdv()
##Left Route        
def leftRoute():
    print("you open the door to the left, and you enter the Expo Room One but no Expo here!")
    roomLeft()
##Right Route    
def rightRoute():
    print("you open the door to the right, and and you enter the Expo Room Two looks like the Contenters will have showcases later.")
    roomRight()
##Back Route   
def backRoute():
    print("you turn back and head home.")
    gameOver()
##Straight Route    
def straightRoute():
    print("you go straight and you see all the games!")
    roomStraightDeathOne
##If you select right route    
def roomRight():
    print("You entered the waiting room for the Content Creators")
    roomRightChoice = input("Please choose one option: Wait, Leave or Sleep")
    if roomRightChoice.upper() == "WAIT":
        print ("You wait and get to meet and see Metal Jesus!")
        winGame()
    elif roomRightChoice.upper() == "LEAVE":
        print ("You leave and forget to come back you don't get to see Metal Jesus.")
        gameOver()
    elif roomRightChoice.upper() == "SLEEP":
        print ("You sleep through the entire Game On Expo")
        gameOver()
##If you select left route            
def roomLeft():
    print("You've entered the random Expo Room you see 3 different ")
    roomLeftChoice = input("Please choose one option: Room 1, Room 2 or Room 3")
    if roomLeftChoice.upper() == "ROOM 1":
        print ("Room 1 is the bathroom however you don't have a Game on Badge and are escorted offsite!")
        gameOver()
    elif roomLeftChoice.upper() == "ROOM 2":
        print ("Room 2 is the Janitor's closet you are in big trouble for going in without a badge.")
        gameOver()
    elif roomLeftChoice.upper() == "ROOM 3":
        print ("You find this Arcade game called Polybius")
        roomLeftDeathOne()
##If left room death            
def roomLeftDeathOne():
    print("The screen is lighting up in an intense psychoactive way you seem addived. There seem to be men in black in the background.")
    roomLeftDeathChoice = input("Do you want to play?")
    if roomLeftDeathChoice.upper() == "YES":
        print ("Your soul is sucked into the Machine and you are forever part of the game")
        gameOver()
    elif roomLeftDeathChoice.upper() == "NO":
        print ("Polybuius doesn't allow you to leave you are forever stuck in the room")
        gameOver()
##If you go straight death     
def roomStraightDeathOne():
    print("You are overwhelmed by Video Games! They are all over the place.")
    roomStraightDeathChoice = input = input("Do you want to play?")
    if roomStraightDeathChoice.upper() == "YES":
        print ("You spend the whole day playing Video Games and miss Metal Jesus!")
        gameOver()
    elif roomStraightDeathChoice.upper() == "NO":
        print ("You get lost in all the Games!")
        gameOver()
##Game Over Function        
def gameOver():
    print("Game Over")
    gameOverChoice = input("Do you want to restart? Type YES or NO")
    if gameOverChoice.upper() == "YES":
        startAdv()
    elif gameOverChoice.upper() == "NO":
        exitGame()
##Win Game Function        
def winGame():
    print("You win, and get to Meet Metal Jesus!")
    exitGame()
##Exit Game Function    
def exitGame():
    exit()
##Call to start the game    
startAdv()
