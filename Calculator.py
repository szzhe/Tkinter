from tkinter import *
from tkinter.ttk import *

class Calculator(object):
    def __init__(self):
        self.root = Tk()
        # self.root.title("Calculator")
        self.root.wm_title("Szzhe教程完整版")  # 修改窗口标题
        self.root.title("Calculator")
        self.root.geometry("700x200+300+250")  # 设置主窗口大小，窗口所在的屏幕位置
        # self.root.maxsize(600, 400)
        # self.root.minsize(300, 240)
        self.root['bg'] = 'darkgray'  # 深灰; 暗灰色
        self.root.resizable(width=False, height=False)  # 设置窗口是否可以变长、边宽，默认为True

        # 添加一个文本框Entry
        self.Entry_num01 = Entry(self.root, font=("微软雅黑", 9, "bold"), width = 10)
        self.Entry_num01.place(x=20, y=80)

        # 添加一个下拉框Combobox
        self.ComboBox_action = Combobox(self.root, font=("微软雅黑", 9, "bold"), width = 5)
        self.ComboBox_action["values"] = ("加[+]", "减[-]", "乘[*]", "除[/]", "余[%]") # 设定可选列表内容
        self.ComboBox_action["state"] = "readonly" # 设定状态。readonly时只可选择，不可修改
        self.ComboBox_action.current(2) # 设定选择内容，参数为可选列表的0-index
        self.ComboBox_action.place(x=110, y=80)

        self.Entry_num02 = Entry(self.root, font=("微软雅黑", 9, "bold"), width = 10)
        self.Entry_num02.place(x=180, y=80)

        # 添加一个标签Lable
        self.Lable_lb = Label(self.root, text = "=", width = 2).place(x=270, y=80)

        self.Entry_result= Entry(self.root, font=("微软雅黑", 9, "bold"), width = 10)
        self.Entry_result["state"] = "disable"
        self.Entry_result.place(x=300, y=80)

        # 添加一个按钮Button。command用户指定一个函数或方法，当用户点击时会触发
        self.Button_cal = Button(self.root, text = "计算", command = self.number_cal, width = 10)
        self.Button_cal.place(x=390, y=80)

    def number_cal(self):
        # global root
        s = Label(self.root, text = "我爱python")
        s.pack(side = RIGHT)

    def show(self):
        self.root.mainloop()  # 事件循环

if __name__ == "__main__":
    User_calculator = Calculator()
    User_calculator.show()