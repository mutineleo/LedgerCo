import abc
class LoanServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addLoan(self,id, principal, no_of_years, rate_of_interest):
        pass