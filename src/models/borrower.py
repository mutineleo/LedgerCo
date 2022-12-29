class Borrower(object):
    def __init__(self):
        self.name = None
        self.bank_name = None
        self.id = None
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setBankName(self, bank_name):
        self.bank_name = bank_name
    
    def getBankName(self):
        return self.bank_name
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id