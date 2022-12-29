import math

class BalanceController(object):
    def __init__(self, balanceService):
        self.balanceService = balanceService
    
    def getBalance(self,id, emi_no):
        balance = 0
        amount = self.balanceService.balanceDetails[id].getAmount()
        emis = self.balanceService.balanceDetails[id].getEmis()
        for i in range(emi_no+1):
            balance += emis[i]
            if balance >= amount:
                balance = amount
                break
        
        months = len(emis)-1
        emi_per_month = math.ceil(amount/months)
        emi_remaining = math.ceil((amount - balance)/emi_per_month)
        
        return (balance,emi_remaining)