from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class Student(Tk):

    file_path = ".//Image//Student.txt"
    student_list = []

    male_number = 0
    female_number = 0

    def __init__(self):
        # 如果类变量student_list数据为空，需要导入；如果不为空，不需要导入数据
        if len(Student.student_list) == 0:
            self.load_student()

    def load_student(self):
        try:
            with open(file=Student.file_path, mode="r", encoding="UTF-8") as fd:
                current_line = fd.readline()
                while current_line:
                    student_info = current_line.split(",")
                    # 判断男女
                    if student_info[2] == "男":
                        Student.male_number += 1
                    else:
                        Student.female_number += 1
                    # 把当前的学生添加到类变量student_list中
                    Student.student_list.append(student_info)
                    current_line = fd.readline()
        except:
            showinfo("系统消息", "读取文件信息出现异常!")

if __name__ == "__main__":
    this_student = Student()