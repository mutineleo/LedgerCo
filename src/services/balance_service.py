from src.services.balance_service_interface import BalanceServiceInterface
from src.models.balance import Balance


class BalanceService(BalanceServiceInterface):
    balanceDetails = {}
    def setBalance(self, id, amount, emis):
        balance = Balance()
        balance.setId(id)
        balance.setAmount(amount)
        balance.setEmis(emis)
        self.__class__.balanceDetails[id] = balance
        return balance
