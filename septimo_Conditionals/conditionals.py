#Conditionals are used to compare pieces of information, it can create different paths through the program.

#they are "if", "else" and "elif"

userReply = input("Do you need to ship a package? (Enter yes or no) ")

#python uses spacing to determine the start and end of a logic block.

#the "==" symbol is used to compare two pieces of information.

if  userReply == "yes":
    print("We can help you ship that package!")

else:
    print("Please come back when you need to ship a package. Thank you.") 

#the "elif" statement always comes after an "if" statement and before the "else" statement.

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")