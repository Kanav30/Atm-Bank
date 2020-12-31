class Atm(object):
    def __init__(self,atmCarNumber,pinNumber):
        self.atmCarNumber = atmCarNumber
        self.pinNumber = pinNumber
    
    def CashWithdrawal(self):
        print("Cash WithDrawl Started")

    def BalanceEnquiry(self):
        print("Your Balance = $300")
    
    def Help(self):
        print("For Help pls call on ##########")

Kanav = Atm(10234582,1023)
print(Kanav.pinNumber)