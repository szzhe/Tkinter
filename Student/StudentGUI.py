from tkinter import *
from tkinter.ttk import *
import Student

class StudentGUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("计算学生人数")
        self.geometry("600x585+700+90")
        self.resizable(width=False, height=False)  # self.resizable(0, 0)
        self["bg"] = "lightgray"

        # 自动加载窗体
        self.setup_UI()
        # 自动加载学生信息
        self.load_Student_info()

    def setup_UI(self):

        self.Style01 = Style()
        self.Style01.configure("title.TLabel", font=("微软雅黑", 12, "bold"))
        self.Style01.configure("TLabel", font=("微软雅黑", 10, "bold"), foreground="navy", background="lightgray")

        self.TopLable = PhotoImage(file=".//Image//stu_detail_top_banner01.png")
        self.Lable_image = Label(self, image=self.TopLable)
        self.Lable_image.place(x=0, y=0)

        self.Lable_title = Label(self, text="==学生信息统计列表==", style="title.TLabel")
        self.Lable_title.place(x=20, y=30)

        self.Lable_title = Label(self, text="总人数：")
        self.Lable_title.place(x=20, y=123)

        self.var_total = StringVar()
        self.Entry_total = Entry(self, textvariable=self.var_total, state=DISABLED, font=("微软雅黑", 9, "bold"), width=8)
        self.Entry_total.place(x=75, y=120)

        self.Lable_title = Label(self, text="男生人数：")
        self.Lable_title.place(x=180, y=123)

        self.var_male = StringVar()
        self.Entry_total = Entry(self, textvariable=self.var_male, state=DISABLED, font=("微软雅黑", 9, "bold"), width=8)
        self.Entry_total.place(x=245, y=120)

        self.Lable_title = Label(self, text="女生人数：")
        self.Lable_title.place(x=340, y=123)

        self.var_female = StringVar()
        self.Entry_total = Entry(self, textvariable=self.var_female, state=DISABLED, font=("微软雅黑", 9, "bold"), width=8)
        self.Entry_total.place(x=405, y=120)

        # 添加Treeview控件
        self.Tree = Treeview(self, columns=("sno", "name", "gender", "birthday", "mobile"), show="headings", height=20)

        # 设置每一个列的宽度和对其方式
        self.Tree.column("sno", width=100, anchor="center")
        self.Tree.column("name", width=120, anchor="center")
        self.Tree.column("gender", width=60, anchor="center")
        self.Tree.column("birthday", width=120, anchor="center")
        self.Tree.column("mobile", width=180, anchor="center")

        # 设置每个列的标题
        self.Tree.heading("sno", text="学号")
        self.Tree.heading("name", text="姓名")
        self.Tree.heading("gender", text="性别")
        self.Tree.heading("birthday", text="出生日期")
        self.Tree.heading("mobile", text="手机号码")

        self.Tree.place(x=10, y=160)

    def load_Student_info(self):
        # 0.实例化操作学生类
        this_student = Student.Student()

        # 1.填充人数
        self.var_male.set(Student.Student.male_number)
        self.var_female.set(Student.Student.female_number)
        self.var_total.set(Student.Student.male_number + Student.Student.female_number)

        # 2.导入数据到表格
        for i in self.Tree.get_children():
            self.Tree.delete(i)

        list_student = Student.Student.student_list
        # 遍历List逐条插入
        for index in range(len(list_student)):
            self.Tree.insert("", index, value=(list_student[index][0], list_student[index][1], list_student[index][2],list_student[index][3], list_student[index][4]))

if __name__ == "__main__":
    this_gui = StudentGUI()
    this_gui.mainloop()