

from src.controllers.balance_controller import BalanceController
from src.controllers.borrower_controller import BorrowerController
from src.controllers.loan_controller import LoanController
from src.controllers.payment_controller import PaymentController

from src.services.balance_service import BalanceService
from src.services.borrower_service import BorrowerService
from src.services.loan_service import LoanService

balanceController = BalanceController(BalanceService())
borrowerController = BorrowerController(BorrowerService())
loanController = LoanController(LoanService(),BalanceService())
paymentController = PaymentController(BalanceService())

class Driver(object):
    def __init__(self):
        self.free_id = 1
    
    def PAYMENT(self, id, amount, emi_no):
        paymentController.addPayment(id,amount,emi_no)

    def LOAN(self,id,principal, no_of_years, rate_of_interest):
        loanController.addLoan(id, principal, no_of_years, rate_of_interest)

    def BALANCE(self, id, emi_no):
        return balanceController.getBalance(id, emi_no)

    def addBorrowerId(self, name, bank_name, free_id):
        borrowerController.addBorrower(free_id,name,bank_name)

    def runApp(self, Lines):
        results = []
        for line in Lines:
            commands = line.split()
            bank_name = commands[1]
            borrower_name = commands[2]
            if commands[0] == 'LOAN':
                self.addBorrowerId(borrower_name,bank_name, self.free_id)
                self.free_id += 1
                id = borrowerController.borrowerService.borrowerDetails.get((borrower_name,bank_name))
                principal = int(commands[3])
                no_of_years = int(commands[4])
                rate_of_interest = int(commands[5])
                self.LOAN(id, principal, no_of_years, rate_of_interest)
            elif commands[0] == 'PAYMENT':
                id = borrowerController.borrowerService.borrowerDetails.get((borrower_name,bank_name))
                lump_sum_amount = int(commands[3])
                emi_no = int(commands[4])
                self.PAYMENT(id, lump_sum_amount, emi_no)
            else:
                id = borrowerController.borrowerService.borrowerDetails.get((borrower_name,bank_name))
                emi_no = int(commands[3])
                amount_paid, no_of_emis_left = self.BALANCE(id, emi_no)
                results.append([bank_name, borrower_name, str(amount_paid), str(no_of_emis_left)])
        return results

    def startApp(self,Lines):
        results = self.runApp(Lines)
        for result in results:
            print(*result)