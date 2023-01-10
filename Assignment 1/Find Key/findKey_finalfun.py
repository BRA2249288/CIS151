colorinv = []
def checkColor():
    ## 4 tries to guess
    for i in range(4):
        ##Getting the input and if it matches to an if else appends 
        color = input ("Guess the 3 colors 'Hint traffic light'")     
        if 'green' in color:
            print("Green color found")
            checkResult(color)
            break  
        elif 'red' in color:
            print("Red color found")
            checkResult(color)
            break
        elif 'yellow' in color:
            print("Yellow color found")
            checkResult(color)
            break
        else:
            if i < 2:
                print("Try Again")
            else:
                print("Sorry, to many guesses..You Lose")

##Triggers both the check answer to run again and check color to get next input            
def checkResult(color):
    AppendColor(color)
    checkAnswer()
    checkColor()

##If matches adds to the list 
def AppendColor(color):
    colorinv.append(color)
    
##This checks the answer to see if they have guessed all the colors correctly                
def checkAnswer():
        if 'green' in colorinv and 'yellow' in colorinv and 'red' in colorinv:
            print("You guessed all Colors correctly ")
            print("You Win!")
            exit()
    
checkColor()
    
