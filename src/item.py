class Item:
    def __init__(self, itemName):
        self.itemName = itemName
        # self.description = description
    
    def on_take(self):
        print(f"Player picked up the {self.itemName}")
        return self.itemName

    def on_drop(self):
        print(f"Player put back the {self.itemName}")
        return self.itemName