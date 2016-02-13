######################################################################
# Name: Dillan Johnston                                              #
# Date: 2/7/16                                                       #
# Description: Room Adventure Game                                   #
######################################################################

######################################################################
# the blueprint for a room
class Room(object):
    # the constructor
    def __init__(self, name):
        #rooms have a name, exits, exit locations, items, item descriptions, and grabbables
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    # adds an item to the room
    # the item is a string
    # the desc is a string that descripbes the item
    def addItem(self, item, desc):
        # append the tiem and secription to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string
    def addGrabbable(self, item):
    # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string
    def delGrabbable(self, item):
        # remove the tiem from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)

        # next, the items in the room
        s += "You see:"
        for item in self.items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s

def createRooms():
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom

    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    # add exits to room 1
    r1.addExit("east", r2) 
    r1.addExit("south", r3)
    #add grabbables to room 1
    r1.addGrabbable("key")
    # add items to room 1
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")

    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")

    # add exits to room 3
    r3.addExit("north",r1)
    r3.addExit("east", r4)
    # add grabbables to room 3
    r3.addGrabbable("book")
    # add items to room 3
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")

    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)   # Death
    # add items to room 4
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1

    
        
######################################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # create the rooms

# play forever
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYour are carrying: {}\n".format(currentRoom,inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    # exit the game
    if (currentRoom == None):
        #death()
        break
    # display the status
    print "=========================================================="
    print status

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    # we use raw_input here to treat the input as a string instead of
    # an expression
    action = raw_input("What to do? ")

    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to know values
    action = action.lower()

    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    # split the user input into words (words are separated by spaces)
    # and store the words in a list
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words [0]
        noun = words [1]

        # the verb is: go
        if (verb == "go"):
            # set a defualt response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]

                    # set the response (success)
                    response = "Room changed."

                    # no need to check any more exits
                    break
            # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break

        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # if a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's inventroy
                    inventory.append(grabbable)

                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable items
                    break
    # display the response
    print "\n{}".format(response)
        


