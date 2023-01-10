"""  SpicesRager.py
     A Text based style adventure game
     You're a Rescue Dog Spice ready to have a party!
     """
"""
 Start Game: Has to get party influence to throw an epic rager! Has a time limit! 
"""
##This is where the Game will start it automatically starts 
def gameStart():
    start_Text = """
    You're Spice! A rescue dog that Roommates aka Parents are going out of town. You plan on having a party. You have to figure out what you want to do first?"""
    introText = """Spice’s Roommates aka Parents leave for the day. Spice needs dogs treats, brew, food and guests to throw a rager! """
    introChoice = """Do you go to the backyard? Do you go upstairs? Do you jump in the pool? Do you sleep on the sofa? Do you steal all the dog toys?
    Do you use the Roommate aka “Rent’s” cell phone? Do you get a tasty Dog Frozen treat? """
    print(start_Text)
    print(introText)  
##Game variables
keepGoing = True
totalTime = 5
partyInfluence = 5
partyCount = 0
hasGameStarted = 0
##This is called to subtract time :(
def loseTime():
    print("You lose time")
    global totalTime
    totalTime -= 1
    ifGameOver()
##Call Game over to see if it's over    
def ifGameOver():
    if totalTime != 0:
       print("You only have %d time left!" % totalTime)
       choiceDef()
    else:
       gameOver()
##This is called to add party influence!         
def gainParty():
    print("You gained Party Influence!")
    global partyCount
    partyCount += 1
    ifWinGame()     
##Checks to see if you won the game    
def ifWinGame():
    if partyCount == partyInfluence:
       winGame()
    else:
       print("You have %d party influence " % partyCount)
       choiceDef()
##This is for the choice backyard
def goToBackyard():
    print("You go to the Backyard. Do you hide in the Cat House? Prepare some BBQ? Chill out in the Hot Tub?")
    goToBackyardChoice = input("Please choose one option: Cat, BBQ or Hot")
    if goToBackyardChoice.upper() == "CAT":
        print ("You choose the Cat House you fall asleep. You lose time.")
        loseTime()
    elif goToBackyardChoice.upper() == "BBQ":
        print ("You choose to make BBQ. Your guests will all have amazing food.")
        gainParty()
    elif goToBackyardChoice.upper() == "HOT":
        print ("You choose to chill out in the Hot Tub although fun you lose track of Time. ")
        loseTime()
##This is for if you choose upstairs
def goToUpstairs():
    print("You go Upstairs. Do you go into the Bedroom? Do you go into the Game Room? Do you go into the bathroom?")
    goToUpstairsChoice = input("Please choose one option: Bed, Game or Bath")
    if goToUpstairsChoice.upper() == "BED":
        print ("You went into the bedroom and take a nap. You lose time.")
        loseTime()
    elif goToUpstairsChoice.upper() == "GAME":
        print ("You go into the Game Room and find some epic Video Games to play for the party.")
        gainParty()
    elif goToUpstairsChoice.upper() == "BATH":
        print ("You go into the bathroom. You spend too much time and lose time.")
        loseTime()
##Did you choose the pool? You go here
def goToPool():
    print("You Jump into the pool. Do you setup the floating beer pong table? Swim? Take a nap on the floating lounger?")
    goToPoolChoice = input("Please choose one option: Beer, Swim or Float")
    if goToPoolChoice.upper() == "BEER":
        print ("You setup the epic beer pong table and create a Snap Chat video inviting your friends.")
        gainParty()
    elif goToPoolChoice.upper() == "SWIM":
        print ("You swim and lose track of time.")
        loseTime()
    elif goToPoolChoice.upper() == "FLOAT":
        print ("You fall asleep on the floating lounger and lose time.")
        loseTime()
##Did you go to the sofa? You would end up here
def goToSofa():
    print("You go to the sofa. You take a Quick Power Nap. You wake up do you keep napping?")
    goToSofaChoice = input("Please choose one option: Yes or No")
    if goToSofaChoice.upper() == "YES":
        print ("You setup the epic beer pong table and create a Snap Chat video inviting your friends.")
        loseTime()
    elif goToSofaChoice.upper() == "NO":
        print ("You swim and lose track of time.")
        gainParty()
##Did you want dog toys? You find yourself with a choice to share or not!
def goToDogToys():
    print("You steal all the Dog Toys. Do you share with the other dogs? ")
    goToDogToysChoice = input("Please choose one option: Share or NoShare")
    if goToDogToysChoice.upper() == "NOSHARE":
        print ("The other dogs are angry you didn’t share. You lose time fighting with them.")
        loseTime()
    elif goToDogToysChoice.upper() == "SHARE":
        print ("For sharing your toys, the other dogs decide to help you throw an epic party.")
        gainParty()
##Who doesn't like cell phones? You end up here if you choose Cell phone
def goToCellPhone():
    print("You take the Roommates Cell Phone. Do you Order Pizza? Do you Order a Keg? Do you call the neighbor dog?")
    goToCellPhoneChoice = input("Please choose one option: Pizza, Keg or Dog")
    if goToCellPhoneChoice.upper() == "PIZZA":
        print ("You end up order a bunch of pizzas for everyone. People alone will come for the Pizza. Even if it’s the TMNT.")
        gainParty()
    elif goToCellPhoneChoice.upper() == "KEG":
        print ("You order a Keg. You will throw the most epic party.")
        gainParty()
    elif goToCellPhoneChoice.upper() == "DOG":
        print ("You waste time talking with the neighbor dog.")
        loseTime()
##Yum treats if you choose treats you end up here!
def goToTreats():
    print("You take out the Box of Tasty Treats. Do you share? Do you eat the treat in front of the other dogs? You eat all the treats?")
    goToTreatsChoice = input("Please choose one option: Share, Eat or All")
    if goToTreatsChoice.upper() == "SHARE":
        print ("You Share your treats all the dogs help you throw an epic party.")
        gainParty()
    elif goToTreatsChoice.upper() == "EAT":
        print ("You don’t share all the dogs fight with you. You lose Time.")
        loseTime()
    elif goToTreatsChoice.upper() == "ALL":
        print ("You eat all the treats and lose time because you are so full.")
        loseTime()
##Choice function called to see what your next move will be
def choiceDef():
    choice = input("Choose 'back' for Backyard or 'up' for Upstairs or 'jump' for Pool or 'sleep' for Sofa or 'toys' for Toys or 'cell' for CellPhone or 'treat' for Treat ")
    if choice.upper() == "BACK":
        goToBackyard()
    elif choice.upper() == "UP":
        goToUpstairs()
    elif choice.upper() == "JUMP":
        goToPool()
    elif choice.upper() == "SLEEP":
        goToSofa()
    elif choice.upper() == "TOYS":
        goToDogToys()
    elif choice.upper() == "CELL":
        goToCellPhone()
    elif choice.upper() == "TREAT":
        goToTreats()
    elif choice.upper() == "START":
        gameStart()
##Game over happens here        
def gameOver():
    gameOverText() 
    gameOverChoice = input("Do you want to restart? Type YES or NO")
    if gameOverChoice.upper() == "YES":
        hasGameStarted = 0 
    elif gameOverChoice.upper() == "NO":
        exitGame()
##If you win this happens        
def winGame():
    winGameText()
    exitGame() 
##Win Game Text stored here 
def winGameText():
    winGameText = """You win, and spice gets his Epic Rager the whole neighborhood shows up plus Spice's Snapchat buddies!"""
    print(winGameText)
##Lose Game Text goes here
def gameOverText():
    gameOverText = """Game Over :( you ran out of time and spice was grounded for trying to throw a party. """
    print(gameOverText)
##Exit the game
def exitGame():
    exit()        
##Global choice global means you can access this variable anywhere
global choice
##Game Loop to keep the game going
while keepGoing:
    if partyInfluence > 0 :
     if hasGameStarted == 1:    
        choiceDef()
     elif hasGameStarted == 0:
         hasGameStarted = 1
         gameStart()
    else:
         print("Sorry, you don't have any party influence")
         keepgoing = False




