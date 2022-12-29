import abc
class BorrowerServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBorrower(self,id,name,bank_name):
        pass