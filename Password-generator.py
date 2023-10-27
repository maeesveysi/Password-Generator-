import string 
import random

characters = list (string.ascii_letters + string.digits + "!@#$%&*")

def generate_password ():
    pawwsord_lenght = int (input (' How Long Would You Like your Password ? '))

    random.shuffle(characters)

    password = []

    for x in range (pawwsord_lenght) :
        password.append (random.choice (characters))

    random.shuffle (password)

    password = "".join(password)

    print (password)

option= input(" Do you Want  to generate a password ? (Yes / No)")

if option == 'Yes' or 'yes' :
    generate_password()

elif option == "No" or 'no':
    print ("Program Ended")
    quitno()

else :
    print ('invalid Inputcls')
    quit()
