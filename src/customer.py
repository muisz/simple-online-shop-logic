class Address:
    country: str
    state: str
    city: str
    postCode: str

    def __init__(self, country, state, city, postCode):
        self.country = country
        self.state = state
        self.city = city
        self.postCode = postCode
    
    def showAddressInfo(self):
        print('Country\t\t: ', self.country)
        print('State\t\t: ', self.state)
        print('City\t\t: ', self.city)
        print('Post code\t: ', self.postCode)

class Wallet:
    balance: float
    pin: str

    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
    
    def checkPinNumber(self):
        pinNumber = input('Enter pin number: ')
        if not self.isValidPinNumber(pinNumber):
            raise Exception('invalid pin number')
        return
    
    def checkAmount(self, amount):
        if amount > self.balance:
            raise Exception('running out of balance')
    
    def isValidPinNumber(self, pinToCheck: str):
        return pinToCheck == self.pin
    
    def topup(self, amount: float):
        self.checkPinNumber()
        self.balance += amount
    
    def paid(self, amount: float):
        self.checkPinNumber()
        self.checkAmount(amount)
        self.balance -= amount
    
    def showWalletInfo(self):
        print('========================')
        print('balance\t: ', self.balance)
        print('========================')

class Customer:
    firstName: str
    lastName: str
    email: str
    address: Address
    wallet: Wallet

    def __init__(self, firstName: str, lastName: str, email: str, address: Address, wallet: Wallet):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.address = address
        self.wallet = wallet
    
    @property
    def name(self):
        return self.firstName + ' ' + self.lastName
    
    def setAddress(self, newAddress):
        self.address = newAddress
    
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastname(self, lastName):
        self.lastName = lastName
    
    def setEmail(self, email):
        self.email = email

    def isValidateAddress(self, address):
        return isinstance(address, Address)
    
    def hasAddress(self):
        return self.address is not None
    
    def showCustomerInfo(self):
        print('===========================================')
        print('First name\t: ', self.firstName)
        print('Last name\t: ', self.lastName)
        print('Email\t\t: ', self.lastName)
        if self.hasAddress():
            self.address.showAddressInfo()
        print('===========================================')
    
    @staticmethod
    def registerCustomer(firstName, lastName, email, country, state, city, postCode, pinNumber):
        customerAddress = Address(country, state, city, postCode)
        wallet = Wallet(pinNumber)
        newCustomer = Customer(firstName, lastName, email, customerAddress, wallet)
        return newCustomer
