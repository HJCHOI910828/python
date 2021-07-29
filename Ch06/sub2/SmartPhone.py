from Ch06.sub2.Computer import Computer

class SmartPhone(Computer):

    def __init__(self, cpu, ram, hdd, brand, tel):
        super().__init__(cpu, ram, hdd)
        self.__brand = brand
        self.__tel = tel

    def call(self):
        print('%s call...' % self.__tel)

    def info(self):
        print('모델명 : ', self.__brand)
        print('폰번호 : ', self.__tel)
        print('CPU : ', self.cpu)
        print('RAM : ', self.ram)
        print('HDD : ', self.hdd)
