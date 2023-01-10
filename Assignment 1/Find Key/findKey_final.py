keyinv = []

def checkKey():
    for i in range(3):
        key = input ("you have pulled a key from your inventory. What is the color?")     
##        print (keyinv)

        if 'green' in key:
            print("green key found")
            keyinv.append("green")
            print (keyinv)
            checkUnlock()
            checkKey()
            break  
        if 'red' in key:
            print("red key found")
            keyinv.append("red")
            print (keyinv)
            checkUnlock()
            checkKey()
            break
        if 'yellow' in key:
            print("yellow key found")
            keyinv.append("yellow")
            print (keyinv)
            checkUnlock()
            checkKey()
            break
        else:
            if i < 2:
                print("try again")
            else:
                print("Sorry, to many guesses..")


def checkUnlock():
        if 'green' in keyinv and 'yellow' in keyinv and 'red' in keyinv:
            print("Door Unlocked")
                
        
checkKey()
    
