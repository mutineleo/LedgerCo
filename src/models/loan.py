class Loan(object):
    def __init__(self):
        self.id = None
        self.principal = None
        self.no_of_years = None
        self.rate_of_interest = None
    
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id
    
    def setPrincipal(self, principal):
        self.principal = principal
    
    def getPrincipal(self):
        return self.principal
    
    def setNoOfYears(self, no_of_years):
        self.no_of_years = no_of_years
    
    def getNoOfYears(self):
        return self.no_of_years
    
    def setRateOfInterest(self, rate_of_interest):
        self.rate_of_interest = rate_of_interest
    
    def getRateOfInterest(self):
        return self.rate_of_interest
