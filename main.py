from src.customer import Customer
from src.order import Item, Cart, CartGroup

def main():

    # register customer
    customer = Customer.registerCustomer(
        firstName='Abdul',
        lastName='Muis',
        email='abdulmuis@email.com',
        country='Indonesia',
        state='Jawa Barat',
        city='Kabupaten Bogor',
        postCode='16660',
        pinNumber='123456'
    )
    customer.wallet.topup(5000)
    customer.showCustomerInfo()

    # add item
    book = Item('Book', 10, 500)
    milk = Item('Milk', 30, 300)

    # add items to cart
    cartGroup = CartGroup(customer)
    cartGroup.addToCart(book)
    cartGroup.addToCart(book)
    cartGroup.addToCart(book)
    cartGroup.addToCart(milk)
    cartGroup.addToCart(milk)

    # cartGroup.decreaseCartItemQuantity(milk)
    # cartGroup.decreaseCartItemQuantity(milk)
    cartGroup.showCartItem()

    # checkout items
    cartGroup.checkout()

    cartGroup.showCartItem()

    book.showItemInfo()
    milk.showItemInfo()

    cartGroup.addToCart(milk)
    cartGroup.addToCart(milk)
    cartGroup.addToCart(book)
    cartGroup.showCartItem()

    # buy specific item
    cartGroup.checkoutSingleItem(milk)

    cartGroup.showCartItem()
    
    book.showItemInfo()
    milk.showItemInfo()

    # direct buy item without adding to the cart
    CartGroup.directCheckoutItem(customer, book, 3)

    book.showItemInfo()

    customer.wallet.showWalletInfo()
    customer.wallet.showWalletHistory()

if __name__ == '__main__':
    main()
