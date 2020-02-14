from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.
class Room(Item):
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, item_list=None, itemName=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.item_list = ['hatchet','cables','spell','energy']
        super().__init__(itemName)

    def room_name(self):
        return self.name

    def room_description(self):
        return self.description

    def room_inventory(self):
        return self.item_list

    def remove_inventory(self, itemName):
        self.item_list.remove(itemName)
        return self.item_list