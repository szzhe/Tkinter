
from datetime import datetime,date

class IdCheck():
    '''实现身份证校验的功能'''

    def __init__(self, id_number:str):
        self.id_number = id_number
        self.id_list = [] # 把身份证号码分离成4部分

        # 自动执行分离
        self.get_id_list()
        # 自动校验
        self.validate_check_number()
        self.validate_birthday()

    def get_id_list(self):
        # 区域代码
        self.id_list.append(self.id_number[:6])
        # 出生日期
        self.id_list.append(self.id_number[6:14])
        # 顺序码
        self.id_list.append(self.id_number[14:17])
        # 校验码
        self.id_list.append(self.id_number[17:])

    def validate_check_number(self):
        if self.get_check_number() == self.id_list[3]:
            print("校验码正确:", self.get_check_number())
        else:
            print("校验码错误")

    def get_check_number(self):
        number = self.id_number[:17]
        # 每个数值位上要乘的系数
        xi_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 返回的校验码
        check_number = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]

        sum_of_number = 0
        for index in range(len(number)):
            sum_of_number += int(number[index]) * xi_list[index]

        yu_number = sum_of_number % 11
        return check_number[yu_number]

    def validate_birthday(self):
        date_from = datetime(year=1900, month=1, day=1)
        date_to = datetime.today()
        id_birthday = datetime(year=int(self.id_number[6:10]), month=int(self.id_number[10:12]), day=int(self.id_number[12:14]))

        if id_birthday > date_from and id_birthday < date_to:
            print("生日有效")
        else:
            print("生日无效")


if __name__ == "__main__":
    this_check = IdCheck("131082198804050419")

