from .base import *


class SyncPair(SyncBase, Pair):
    def amount(self, amount1=Empty, amount2=Empty):
        """
        Порахувати суми обміну

        :param amount1: Сума в currency1
        :param amount2: Сума в currency2

        :return: list[amount1, amount2, rate]
        """
        return self.connector.pair_amount(self.currency1.code, self.currency2.code, amount1, amount2)
