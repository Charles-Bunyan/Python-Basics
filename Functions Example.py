Numlist = []
import time


#This function lets you choose what you want to do to the list
def Start():
    #Checks what you inputted and fires the function you asked for
    choice = int(input("Would you like to add a number, see the biggest number, see the smallest number, or see the list total? (1/2/3/4)\n"))
    if choice == 1:
        AddNum()
    elif choice == 2:
        BigNum()
    elif choice == 3:
        MinNum()
    elif choice == 4:
        TotalNum()
    else:
        print("Invalid answer, choose either 1,2,3 or 4\n")
        time.sleep(1)
        Start()

def AddNum():
    #Appends an integer you put in, then outputs the full numlist
    Numlist.append(int(input("What number would you like to add?\n")))
    print("Succesful, number list is now",Numlist,"\n")
    #This waits one second before it continues, makes code cleaner
    time.sleep(1)
    #Once it is finished, it goes back to the start to let you choose again, same for all functions.
    Start()


def BigNum():
    #Checks if the list is empty, if it is, it won't fire max(), because you can't use max() on an empty list, same for min() and sum()
    if not Numlist:
        print("Number list is empty, please add something to the list first.\n")
        time.sleep(1)
        Start()
    else:
        print("Biggest number is",max(Numlist),"\n")
        time.sleep(1)
        Start()


def MinNum():
    if not Numlist:
        print("Number list is empty, please add something to the list first.\n")
        time.sleep(1)
        Start()
    else:
        print("Smallest number is",min(Numlist),"\n")
        Start()

def TotalNum():
    if not Numlist:
        print("Number list is empty, please add something to the list first.\n")
        time.sleep(1)
        Start()
    else:
        print("Total num is",sum(Numlist),"\n")
#This fires the start function, because when the code starts, all the above code is ignored because they are functions which have not been fired.
Start()
