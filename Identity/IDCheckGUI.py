from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import IDCheck

class IDCheckGui(Tk):

    def __init__(self):
        self.root = Tk()
        self.root.title("身份信息查询")
        self.root.geometry("700x480+300+80")
        self.root['bg'] = "lightblue"

        self.style01 = Style()
        self.style01.configure("TLabel", font=("微软雅黑", 10, "bold"), foreground="navy", background="lightblue")
        self.style01.configure("TButton", font=("微软雅黑", 10, "bold"), foreground="navy", background="lightblue")

        self.fname = ".//Image//waring.png"
        self.normal_image = PhotoImage(file=self.fname)
        self.Lable_image = Label(self.root, image=self.normal_image)
        self.Lable_image.place(x=10, y=10)

        self.Lable_id_input = Label(self.root, text="请输入身份证号码：")
        self.Lable_id_input.place(x=350, y=30)

        self.var_input =StringVar()
        self.Entry_id_input = Entry(self.root, textvariable=self.var_input, font=("微软雅黑", 12, "bold"), width=20)
        self.Entry_id_input.place(x=350, y=60)

        self.Button_id_input = Button(self.root, text="校验", command=self.get_info, width=6)
        self.Button_id_input.place(x=580, y=60)

        # 信息回显区域
        self.Lable_is_exsit = Label(self.root, text="是否有效：")
        self.Lable_is_exsit.place(x=350, y=180)

        self.var_enable = StringVar()
        self.Entry_id_exsit = Entry(self.root, textvariable=self.var_enable, state=DISABLED, font=("微软雅黑", 8, "bold"), width=6)
        self.Entry_id_exsit.place(x=430, y=180)

        self.Lable_is_exsit = Label(self.root, text="性别：")
        self.Lable_is_exsit.place(x=350, y=220)

        self.var_gender = StringVar()
        self.Entry_gender = Entry(self.root, textvariable=self.var_gender, state=DISABLED, font=("微软雅黑", 8, "bold"), width=6)
        self.Entry_gender.place(x=430, y=220)

        self.Lable_is_exsit = Label(self.root, text="出生日期：")
        self.Lable_is_exsit.place(x=350, y=260)

        self.var_birthday = StringVar()
        self.Entry_id_exsit = Entry(self.root, state = DISABLED, textvariable=self.var_birthday, font=("微软雅黑", 8, "bold"), width=18)
        self.Entry_id_exsit.place(x=430, y=260)

        self.Lable_is_area = Label(self.root, text="所在地：")
        self.Lable_is_area.place(x=350, y=300)

        self.var_area = StringVar()
        self.Entry_id_birthday = Entry(self.root, state=DISABLED, textvariable=self.var_area, font=("微软雅黑", 8, "bold"), width=18)
        self.Entry_id_birthday.place(x=430, y=300)

        self.Button_id_close = Button(self.root, text="关闭", command=self.close_window, width=6)
        self.Button_id_close.place(x=580, y=400)

    def show(self):
        self.root.mainloop()

    def close_window(self):
        self.root.destroy()

    def get_info(self):
        id_number = self.var_input.get()
        if len(id_number) == 18:
            check_id = IDCheck.IdCheck(id_number)
            if check_id.is_true_id_number == 0 or len(check_id.birthday) == 0 or len(check_id.area_name) == 0:
                self.var_enable.set("无效")
            else:
                self.var_enable.set("有效")
                self.var_gender.set(check_id.gender)
                self.var_birthday.set(check_id.birthday)
                self.var_area.set(check_id.area_name)
        else:
            showinfo("系统消息", "身份证号码不满18位，请重新输入")
