from src.models.borrower import Borrower
from src.services.borrower_service_interface import BorrowerServiceInterface


class BorrowerService(BorrowerServiceInterface):
    borrowerDetails = {}
    def addBorrower(self, id, name, bank_name):
        borrower = Borrower()
        borrower.setId(id)
        borrower.setName(name)
        borrower.setBankName(bank_name)
        self.__class__.borrowerDetails[(name,bank_name)] = borrower
        return borrower