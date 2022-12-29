import math

class LoanController(object):
    def __init__(self, loanService, balanceService):
        self.loanService = loanService
        self.balanceService = balanceService
    
    def addLoan(self, id, principal, no_of_years, rate_of_interest):
        
        self.loanService.addLoan(id, principal, no_of_years, rate_of_interest)
        amount = math.ceil(principal*(1+no_of_years*rate_of_interest/100))
        months = no_of_years*12
        emi_per_month = math.ceil(amount/months)
        emis = [emi_per_month]*(months+1)                                #setting emi per month in list
        emis[0] = 0
        emis[months] -= (emi_per_month*months - amount)            #subtracting the extra amount added to last months
        self.balanceService.setBalance(id, amount, emis)
