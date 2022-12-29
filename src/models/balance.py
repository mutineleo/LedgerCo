class Balance(object):
    def __init__(self):
        self.id = None
        self.amount = None
        self.emis = []
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
        
    def setAmount(self, amount):
        self.amount = amount
    
    def getAmount(self):
        return self.amount
    
    def setEmis(self, emis):
        self.emis = emis
    
    def getEmis(self):
        return self.emis