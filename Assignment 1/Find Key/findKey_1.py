keyinv = []

def checkKey():
    for i in range(3):
        key = input ("you have pulled a key from your inventory. What is the color?")

        keyinv.append(key)
##        print (keyinv)

        if 'green' in keyinv:
            print("the door has opened")
            break
        else:
            if i < 2:
                print("try again")
            else:
                print("Sorry, to many guesses..")
                checkKey()
        
checkKey()
    
