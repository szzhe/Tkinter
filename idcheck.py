
from datetime import datetime
import sys
from tkinter.messagebox import *

class IdCheck():
    '''实现身份证校验的功能'''

    def __init__(self, id_number:str):
        self.id_number = id_number
        self.id_list = [] # 把身份证号码分离成4部分

        self.file_path = sys.path[0] + "\\Image\\idarea.txt"
        self.area_list = []

        self.is_true_id_number = 0
        self.gender = ""
        self.birthday = ""
        self.area_name = ""

        # 自动执行分离
        self.get_id_list()
        # 自动加载区域信息
        self.import_area_id()

        # 自动校验
        self.validate_verification_code()
        self.validate_birthday()
        self.validate_area_id()
        self.get_gender()

    def get_id_list(self):
        # 区域代码
        self.id_list.append(self.id_number[:6])
        # 出生日期
        self.id_list.append(self.id_number[6:14])
        # 顺序码
        self.id_list.append(self.id_number[14:17])
        # 校验码
        self.id_list.append(self.id_number[17:])

    def validate_verification_code(self):
        if self.get_check_number() == self.id_list[3]:
            # print("校验码正确:", self.get_check_number())
            self.is_true_id_number = 1
        # else:
        #     print("校验码错误")

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
            # print("生日有效", date_from, date_to, id_birthday)
            self.birthday = self.id_number[6:10] + "年" + self.id_number[10:12] + "月" + self.id_number[12:14] + "日"
        else:
            print("生日无效")

    def import_area_id(self):
        try:
            with open(file=self.file_path, mode="r",) as fd:
                current_line = fd.readline()
                while current_line:
                    current_area_list = current_line.split("\t")
                    if len(current_area_list[0]) == 6:
                        self.area_list.append(current_area_list)
                    current_line = fd.readline()
        except:
            showinfo("系统消息", "读取文件异常")

    def validate_area_id(self):
        for index in range(len(self.area_list)):
            if self.area_list[index][0] == self.id_list[0]:
                # print(self.area_list[index][1])
                self.area_name = self.area_list[index][1]
                break
            # if index == len(self.area_list)-1:
            #     print("地区码不存在")

    def get_gender(self):
        if int(self.id_list[2]) % 2 == 0:
            self.gender = "女"
        else:
            self.gender = "男"

if __name__ == "__main__":
    this_check = IdCheck("131082198804050419")

