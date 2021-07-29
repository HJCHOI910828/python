class Account:

    def __init__(self, bank, id, name, money):
        self._bank = bank # __캡슐화 private _protected
        self._id = id
        self._name = name
        self._money = money

    def deposit(self, money):
        self._money += money
        print()

    def withdraw(self, money):
        self._money -= money

    def show(self):
        print('=============')
        print('은행명 :', self._bank)
        print('계좌번호 :', self._id)
        print('입금주 :', self._name)
        print('현재잔액 :', self._money)
        print('-------------')

    pass


