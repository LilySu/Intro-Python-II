from room import Room
from player import whatRoomIn
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player_location = room['outside']
print("""+----------------------+/n
|           |-|         |
|           |-|  ****   |
|  Overlook |-|Treasure |
|           |-|  ****   |
|           |-|         |
+----   ----------  ----+
|            |          |
|            |          |
|    Foyer      Narrow  |
|            |          |
|            |          |
+----   ----------------+
|            |
|            |
|   Outside  |
|      ^     |
|    Start   |
+------------+""")
player = input("please input player name:")

# Write a loop that:
while True:
    current_room = player_location.room_name()
    print(f"|||||-----{current_room}-----|||||")
    print(f"|||---{player_location.room_description()}---|||")

    room_inventory = player_location.room_inventory()
    print(f"\n\n ~*~*~ Here are what is available in the room: {room_inventory} ~*~*~ ")
    print(f" ~*~ Please input 'get' then the item you want from the loot in the room. ~*~ ")
    cmd = input(" ~*~*~ Please input a cardinal direction n, s, e, w:  ~*~*~ ")

    player_property = whatRoomIn(player, current_room)
    player_name, player_current_room = player_property.show_player_properties()
    print(f"\n\n ~~ Player {player_name} is currently in the {player_current_room}. ~~ \n\n")

# If the user enters a cardinal direction, attempt to move to the room there.
    direction = {'n': player_location.n_to ,'s': player_location.s_to,'e': player_location.e_to,'w': player_location.w_to}
    if cmd in direction.keys():
        if direction[cmd] != None:
            player_location = direction[cmd]
        else:
            print('----------Bumped into wall. Please try another direction: n,s,e or w!----------')
    # elif 'get' in cmd:
    #     cmd_as_list = list(cmd.split(' '))
    #     num_words = len(cmd_as_list)
    #     if num_words > 1:
    #         player_wants_to_get = cmd_as_list[1]
    #         if player_wants_to_get in room_inventory:
    #             new_item = Item(player_wants_to_get)# item gets passed in here
    #             new_item_to_store = new_item.on_take()

    #             player_possesses = player_property.player_inventory()
    #             print(f"Player already had {player_possesses} and now possess {player_property.player_added_to_inventory(new_item_to_store)}.")
    #             room_inventory = player_location.remove_inventory(player_wants_to_get)
    #             print(f"\n\n ~*~*~ Here are what is available in the room: {room_inventory} ~*~*~ ")
    #         else:
    #             print(f"{player_wants_to_get} is not in the room.")
    #     else:
    #         print('Please write get item, 2 words total.')
    elif cmd == 'inventory':
        player_possesses = player_property.player_inventory()
        print(player_possesses)
    elif cmd == "q":
        print("Goodbye!")
        break
# Print an error message if the movement isn't allowed
    else:
        print("Invalid selection. Please try again.")