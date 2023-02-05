from typing import List
from datetime import datetime
from enum import Enum

from src.customer import Customer
from src.item import Item


class Cart:
    item: Item
    customer: Customer
    quantity: int
    minimum_quantity = 1

    def __init__(self, item: Item, customer: Customer):
        self.item = item
        self.customer = customer
        self.quantity = 1
    
    def isQuantityLessThanMinimum(self):
        return self.quantity < 1
    
    def increaseQuantity(self):
        self.quantity += 1
    
    def decreaseQuantity(self):
        if not self.isQuantityLessThanMinimum():
            self.quantity -= 1

    def setQuantity(self, newQuantity):
        self.quantity = newQuantity

class Payment:
    customer: Customer
    carts: List[Cart]
    createdAt: datetime

    def __init__(self, customer, carts: List[Cart]):
        self.customer = customer
        self.carts = carts
    
    @property
    def total_amount(self):
        total = 0
        for cart in self.carts:
            total += cart.item.price * cart.quantity
        return total

    def checkoutPayment(self):
        total_amount = self.total_amount
        print('total amount\t: ', total_amount)
        self.customer.wallet.paid(total_amount)
        self.updateItemQuantity()
        self.createdAt = datetime.today()
        print('============')
        print('payment success!')
        print('Customer name\t: ', self.customer.name)
        print('Total Item\t: ', len(self.carts))
        print('Payment total\t: ', self.total_amount)
        print('Payment date\t: ', self.createdAt)
        print('============')

    def updateItemQuantity(self):
        for cart in self.carts:
            itemQuantityLeft = cart.item.quantity - cart.quantity
            cart.item.updateQuantity(itemQuantityLeft)

class CartGroup:
    customer: Customer
    carts: List[Cart] = []

    def __init__(self, customer: Customer):
        self.customer = customer
    
    def findItemInCart(self, item: Item):
        for cartIndex in range(len(self.carts)):
            if self.carts[cartIndex].item.id == item.id:
                return cartIndex
        return -1
    
    def isItemInCart(self, item: Item):
        cartIndex = self.findItemInCart(item)
        return cartIndex != -1
    
    def increaseCartItemQuantity(self, item: Item):
        cartIndex = self.findItemInCart(item)
        self.carts[cartIndex].increaseQuantity()
    
    def decreaseCartItemQuantity(self, item: Item):
        cartIndex = self.findItemInCart(item)
        cart = self.carts[cartIndex]
        cart.decreaseQuantity()
        if cart.isQuantityLessThanMinimum():
            self.removeCartWithIndex(cartIndex)
    
    def addToCart(self, item: Item):
        if self.isItemInCart(item):
            self.increaseCartItemQuantity(item)
        else:
            cart = Cart(item, self.customer)
            self.carts.append(cart)
    
    def removeFromCart(self, item: Item):
        if self.isItemInCart(item):
            cartIndex = self.findItemInCart(item)
            self.removeCartWithIndex(cartIndex)
    
    def removeCartWithIndex(self, cartIndex):
        self.carts.pop(cartIndex)
    
    def emptyCart(self):
        self.carts = []

    def showCartItem(self):
        for cart in self.carts:
            print('=========================')
            print('Item Id\t\t: ', cart.item.id)
            print('Item name\t: ', cart.item.itemName)
            print('Item left\t: ', cart.item.quantity)
            print('Cart total\t: ', cart.quantity)
            print('=========================')
    
    @property
    def total_amount(self):
        total = 0
        for cart in self.carts:
            total += cart.item.price * cart.quantity
        return total
    
    def checkoutSingleItem(self, item: Item):
        if self.isItemInCart(item):
            cartIndex = self.findItemInCart(item)
            cart = self.carts[cartIndex]
            CartGroup.directCheckoutItem(self.customer, cart.item, cart.quantity)
            self.removeCartWithIndex(cartIndex)

    def checkout(self):
        payment = Payment(self.customer, self.carts)
        payment.checkoutPayment()
        self.emptyCart()
        return payment

    @staticmethod
    def directCheckoutItem(customer: Customer, item: Item, quantity: int = 1):
        cart = Cart(item, customer)
        cart.setQuantity(quantity)
        payment = Payment(customer, [cart])
        payment.checkoutPayment()
        return payment
