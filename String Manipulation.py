#String Manipulation

Year = input("What was the last 2 digits of the year you entered school?")
Year = str(Year)


Surname = input("What is your first name?")
Surname1 = Surname.upper()
#Using [0] takes the first character of the string, so Hello[0] is "H"
Surname1 = Surname1[0]
Surname2 = Surname.lower()
Surname2 = Surname2[1:5]

Firstname = input("What is your First name?")
Firstname = Firstname[0]

#Using + with strings combines them
print(Year+Surname1+Surname2+Firstname)
