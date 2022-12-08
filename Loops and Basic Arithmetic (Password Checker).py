#Loops and basic arithmetic

guesses = 3
password = "qwerty12345"
solved = False

#While loop to check password until either correct or no guesses left
while guesses > 0:
    passguess = input("Input password ")
    #if password guess is correct, print that its correct and break the loop early

    #Checks to see if password guess is correct, and then breaks the loop
    if passguess == password:
        solved = True
        print("Correct password!")
        break
    #Else, we can assume password is wrong    
    else:
        #If password guess is wrong, take away a guess and print out that its wrong.
        guesses -=1 
        print("Incorrect,",guesses,"guesses left.")

#Once the looped is broken, if the user hasn't solved the password, it prints out that there are no guesses left
if solved == False:
    print("No guesses left")
