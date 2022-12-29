from src.models.loan import Loan
from src.services.loan_service_interface import LoanServiceInterface


class LoanService(LoanServiceInterface):
    loanDetails = {}
    def addLoan(self, id, principal, no_of_years, rate_of_interest):
        loan = Loan()
        loan.setId(id)
        loan.setPrincipal(principal)
        loan.setNoOfYears(no_of_years)
        loan.setRateOfInterest(rate_of_interest)
        self.__class__.loanDetails[id] = loan
        return loan