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

def goToUpstairs():
    print("You go Upstairs. Do you go into the Bedroom? Do you go into the Game Room? Do you go into the bathroom?")
    goToBackyardChoice = input("Please choose one option: Bed, Game or Bath")
    if goToUpstairsChoice.upper() == "BED":
        print ("You went into the bedroom and take a nap. You lose time.")
        loseTime()
    elif goToUpstairsChoice.upper() == "GAME":
        print ("You go into the Game Room and find some epic Video Games to play for the party.")
        gainParty()
    elif goToUpstairsChoice.upper() == "BATH":
        print ("You go into the bathroom. You spend too much time and lose time.")
        loseTime()

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

def goToSofa():
    print("You go to the sofa. You take a Quick Power Nap. You wake up do you keep napping?")
    goToPoolChoice = input("Please choose one option: Yes or No")
    if goToSofaChoice.upper() == "YES":
        print ("You setup the epic beer pong table and create a Snap Chat video inviting your friends.")
        loseTime()
    elif goToSofaChoice.upper() == "NO":
        print ("You swim and lose track of time.")
        gainParty()

def goToDogToys():
    print("You steal all the Dog Toys. Do you share with the other dogs? ")
    goToDogToysChoice = input("Please choose one option: Share or NoShare")
    if goToDogToysChoice.upper() == "SHARE":
        print ("The other dogs are angry you didn’t share. You lose time fighting with them.")
        loseTime()
    elif goToDogToysChoice.upper() == "NOSHARE":
        print ("For sharing your toys, the other dogs decide to help you throw an epic party.")
        gainParty()

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

def goToTreats():
    print("You take the Roommates Cell Phone. Do you Order Pizza? Do you Order a Keg? Do you call the neighbor dog?")
    goToTreatsChoice = input("Please choose one option: Pizza, Keg or Dog")
    if goToTreatsChoice.upper() == "PIZZA":
        print ("You end up order a bunch of pizzas for everyone. People alone will come for the Pizza. Even if it’s the TMNT.")
        loseTime()
    elif goToTreatsChoice.upper() == "KEG":
        print ("You order a Keg. You will throw the most epic party.")
        gainParty()
    elif goToTreatsChoice.upper() == "DOG":
        print ("You waste time talking with the neighbor dog.")
        loseTime()
