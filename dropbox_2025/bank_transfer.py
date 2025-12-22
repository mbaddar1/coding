# https://leetcode.com/problems/simple-bank-system/submissions/1857546873
from typing import List
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(self.balance)
        pass
    def __valid_account(self,account:int):
        return 1 <= account <= self.n
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.__valid_account(account1):
            return False
        if not self.__valid_account(account2):
            return False
        if money > self.balance[account1-1]:
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True
    def deposit(self, account: int, money: int) -> bool:
        if not self.__valid_account(account):
            return False
        self.balance[account-1] += money
        return True
    def withdraw(self, account: int, money: int) -> bool:
        if not self.__valid_account(account):
            # print("withdraw bad account index")
            return False
        if money > self.balance[account-1]:
            # print("withdraw money > balance")
            return False
        self.balance[account-1] -= money
        return True

if __name__=="__main__":
    pass