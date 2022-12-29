class BorrowerController(object):
    def __init__(self, borrowerService):
        self.borrowerService = borrowerService
    
    def addBorrower(self, id, name, bank_name):
        return self.borrowerService.addBorrower(id, name, bank_name)