#TBG Action Menu - Jordanne Gienow
#This program lists possible actions the user can take and gives an output based on their answer 

print("Oh no! you are in your house when you hear a crowd of zombies approaching")               #Prints the context message                         
print("\nPossible things you can do are:")                                                       #Prints the                                           
print("Leave your house and go in one of the following directions:"                              #Prints intro to the list of directions
print(" - North")                                                                                #Prints "North"
print(" - East")                                                                                 #Prints "East"
print(" - South")                                                                                #Prints "South"
print(" - West")                                                                                 #Prints "West"
print("Complete one of these actions:")                                                          #Prints intro to the list of actions
print(" - Fight")                                                                                #Prints "Fight"
print(" - Hide")                                                                                 #Prints "Call for help"
print(" - Call for help")

action = input("\nWhich of these actions would you like to complete? ")                          #Prints a statement that asks the user which action to complete 

if action == "North":                                                                            
    print("\nOkay, you are going North")                                                         #If the user answers "North" prints "you are going North"
elif action == "north":
    print("\nOkay, you are going North")                                                         #If the user answers "north" prints "you are going North"
elif action == "South":
    print("\nOkay, you are going South")                                                         #If the user answers "South" prints "you are going South"
elif action == "south":
    print("\nOkay, you are going South")                                                         #If the user answers "south" prints "you are going South"
elif action == "East":
    print("\nOkay, you are going East")                                                          #If the user answers "East" prints "you are going East"
elif action == "east":
    print("\nOkay, you are going East")                                                          #If the user answers "east" prints "you are going East"
elif action == "West":
    print("\nOkay, you are going West")                                                          #If the user answers "West" prints "you are going West"
elif action == "west":
    print("\nOkay, you are going West")                                                          #If the user answers "west" prints "you are going West"
elif action == "Fight":
    print("\nOkay, you are getting ready to fight")                                              #If the user answers "Fight" prints "you are getting ready to fight"
elif action == "fight":
    print("\nOkay, you are getting ready to fight")                                              #If the user answers "fight" prints "you are getting ready to fight"
elif action == "Hide":
    print("\nYou are getting ready to hide")                                                     #If the user answers "Hide" prints "you are getting ready to hide"
elif action == "hide":
    print("\nYou are getting ready to hide")                                                     #If the user answers "hide" prints "you are getting ready to hide"
elif action == "Call for help":                                                                
    print("\nYou will use your phone to try to call for help")                                   #If the user answers "Call for help" prints a statement about calling for help
elif action == "call for help":
    print("\nYou will use your phone to try to call for help")                                   #If the user answers "call for help" prints a statement about calling for help
elif action == "Call":
    print("\nYou will use your phone to try to call for help")                                   #If the user answers "Call" prints a statement about calling for help
elif action == "call":
    print("\nYou will use your phone to try to call for help")                                   #If the user answers "call" prints a statement about calling for help
else:
    print("\nThis input is invalid. PLease enter one of the options provided")                   #prints an error message if an input is entered that is not from the list
    
