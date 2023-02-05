import random

class Item:
    id: str
    itemName: str
    quantity: int
    price: float
    itemStockLeft: int

    def __init__(self, itemName, quantity, price):
        self.itemName = itemName
        self.quantity = quantity
        self.price = price
        self.itemStockLeft = quantity
        self.id = self.generateItemId()
    
    def generateItemId(self):
        generatedNumber = random.randint(0, 99)
        return f"{generatedNumber}-{self.itemName}"

    def updateQuantity(self, newQuantity: int):
        self.quantity = newQuantity

    def showItemInfo(self):
        print('=========================')
        print('Item Id\t\t: ', self.id)
        print('Item name\t: ', self.itemName)
        print('Item price\t: ', self.price)
        print('Item stock\t: ', self.quantity)
        print('=========================')