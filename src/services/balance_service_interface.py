import abc
class BalanceServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setBalance(self, id, amount,emis):
        pass