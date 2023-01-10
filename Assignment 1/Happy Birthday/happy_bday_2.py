def BirthdaySong():
    #grab user input name
    userName = input("Please type in your name ")
    #if not blank print out name if blank print out no name entered
    if userName != "": 
        print("Happy Birthday to you, ")
        print("Happy Birthday to you, ")
        print("Happy Birthday Dear", userName, ",")
        print("Happy Birthday to you")
    else:
        print("No Name Entered")


#call upon function
BirthdaySong()
