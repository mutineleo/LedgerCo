class PaymentController(object):
    def __init__(self, balanceService):
        self.balanceService = balanceService
    
    def addPayment(self, id, amount, emi_no):
        emis = self.balanceService.balanceDetails[id].getEmis()      
        emis[emi_no] += amount
        self.balanceService.setBalance(id, self.balanceService.balanceDetails[id].getAmount(), emis)