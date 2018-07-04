from tkinter import *
import sys

class IDCheckGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("身份信息查询")
        self.root.geometry("700x550+400+200")
        self.root['bg'] = "lightblue"

        self.fname = sys.path[1] + "\\Image\\timg.png"
        self.normal_image = PhotoImage(file = self.fname)
        self.Lable_image = Label(self.root, image = self.normal_image)
        self.Lable_image.place(x=10, y=10)

        self.Lable_input = Label(self.root, text = "请输入身份证号码：")
        self.Lable_input.place(x=350 , y=20)

        self.Entry_id_input = Entry(self.root, font=("微软雅黑", 16, "bold"), width = 20)
        self.Entry_id_input.place(x=350, y=60)

        self.Button_id_input = Button(self.root, text = "校验", width = 6)
        self.Button_id_input.place(x=630, y=60)

        # 信息回显区域
        self.Lable_is_exsit = Label(self.root, text = "是否有效：")
        self.Lable_is_exsit.place(x=350 , y=180)

        self.Entry_id_exsit = Entry(self.root, state = DISABLED, font=("微软雅黑", 14, "bold"), width = 6)
        self.Entry_id_exsit.place(x=430, y=180)

        self.Lable_is_exsit = Label(self.root, text = "性别：", justify = RIGHT)
        self.Lable_is_exsit.place(x=350 , y=220)

        self.Entry_id_exsit = Entry(self.root, state = DISABLED, font=("微软雅黑", 14, "bold"), width = 6)
        self.Entry_id_exsit.place(x=430, y=220)

        self.Lable_is_exsit = Label(self.root, text = "出生日期：")
        self.Lable_is_exsit.place(x=350 , y=260)

        self.Entry_id_exsit = Entry(self.root, state = DISABLED, font=("微软雅黑", 14, "bold"), width = 18)
        self.Entry_id_exsit.place(x=430, y=260)

        self.Lable_is_area = Label(self.root, text = "所在地：")
        self.Lable_is_area.place(x=350 , y=300)

        self.Entry_id_birthday = Entry(self.root, state = DISABLED, font=("微软雅黑", 14, "bold"), width = 18)
        self.Entry_id_birthday.place(x=430, y=300)

        self.Button_id_input = Button(self.root, text = "关闭", width = 6)
        self.Button_id_input.place(x=610, y=400)


    def show(self):
        self.root.mainloop()

if __name__ == "__main__":
    alice = IDCheckGUI()
    alice.show()