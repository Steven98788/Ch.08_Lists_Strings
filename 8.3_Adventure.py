'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
current_room=0
inventory = []
done= False
#Rooms
room= ["Outside front",1,None,None,None]
room_list. append(room)
room= ["Living Room",None,2,3,None]
room_list. append(room)
room = ["kitchen",4,None,1,None]
room_list. append(room)
room=["play room",6,1,None,None]
room_list. append(room)
room=["dining area",None,None,5,2]
room_list. append(room)
room=["bedroom",None,4,6,None]
room_list. append(room)
room=['Bathroom',None,5,None,3]
room_list. append(room)
#end of rooms

playerName= input("What is your name?")
print("Hello",playerName.center(10))
#navigationsd
while not done:
    print()
    print("current room:",room_list[current_room][0])
    print("Where to", playerName,"?")
    direction = input("\n N for north \n E for east \n S for south \n W for west \n Q to quit \n  ")


    if direction.lower() == 'north' or direction.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
             current_room = next_room

    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
             current_room = next_room

    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room

    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room

    elif direction.lower() == "q":
        print("Thanks for playing!")
        done = True

    else:
        print()
        print("Invalid choice. Please try again.")
        print()
        continue
#End of navigation
    if current_room == 1:
        userInput=input("Would you like to interact with the clock \n i for interact or no to skip")
        if userInput.lower() == "i":
            print("the grandfather clock is moved by many gears")
        elif userInput=="no":
            continue
    if current_room==2:
        userInput=input("")
        userInput.lower()=="i"

