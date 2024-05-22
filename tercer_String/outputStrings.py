#when your script wants to communicate with the user is called output. It will show information to the user.

#create a survey and output the information that it collects back to the user.

name = input("What is your name? ")
color = input("What is your favorite color? ")
animal = input("what is your favorite animal? ")

print("{}, you like a {} {}".format(name, color, animal))