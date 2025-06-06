class Money:

    CURRENCY_VALUES = {
        "20's Note": 20,
        "10's Note/Coin": 10,
        "5's Note/Coin": 5,
        "2's Coin": 2,
        "1's Coin": 1
    }
    def __init__(self):
        self.profit = 0
    
    def report(self):
        '''prints profit'''
        print(f"Total Profit: {self.profit}")

    def process_money(self):
        '''Take input from user, returns total calculated Notes/Coins inserted'''
        print("Please insert Note/Coin")
        money_recieved = 0
        for currency in self.CURRENCY_VALUES:
            money_recieved += int(input(f"How many {currency}?:")) * self.CURRENCY_VALUES[currency]
        return money_recieved

    def make_payment(self, cost):
        '''Returns True if the payment accepted otherwise return False'''
        money_recieved = self.process_money()
        if money_recieved >= cost:
            change = money_recieved - cost 
            if change != 0:
                print(f"Here is ₹{change} change.")
            self.profit += cost 
            return True
        else:
            print("Not enough money! Money Refunded")
            return False
  