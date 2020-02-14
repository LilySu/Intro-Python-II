from item import Item


class whatRoomIn(Item):
    def __init__(self, player_name, current_room, itemName = None, item_list = None):
        self.player_name = player_name
        self.current_room = current_room
        self.item_list = ['ego', 'id']
        super().__init__(itemName)
    
    def show_player_properties(self):
        return self.player_name, self.current_room

    def player_inventory(self):
        return self.item_list

    def player_added_to_inventory(self, itemName):
        self.item_list.append(itemName)

        return self.item_list