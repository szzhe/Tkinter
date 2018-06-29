from tkinter import *

class UToplevel(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Toplevel")

        # 主顶层，作为根被引用
        self.tl = Label(self.root, text='This is the main (default) Toplevel').pack(padx=5,pady=10)

        # 子顶层，依赖于根，若根被破坏，则子顶层也被破坏。普通，无特色。
        self.tl_child = Toplevel()
        Label(self.tl_child, text="This is the child Toplevel").pack(padx=10,pady=15)

        # 临时顶层，总是画于父顶层的顶部，如果浮层被图表化或是最小化之后，则他们被隐藏起来(主窗体缩小时，会跟着一起缩小)
        self.tl_transient = Toplevel()
        Label(self.tl_transient, text="This is a transient windows of root").pack(padx=20,pady=25)
        self.tl_transient.transient(self.root)

        # 未被视窗管理者创建过的顶层可以通过设置一个overrideredirect标志位非零值来创建。该窗口不能被缩放或拖动，不带边框。
        self.tl_overrideredirect = Toplevel(self.root, borderwidth=5, bg="blue")
        Label(self.tl_overrideredirect, text='This is "No wm decorations" windows',bg="blue",fg="white").pack(padx=25,pady=30)
        self.tl_overrideredirect.overrideredirect(1)
        self.tl_overrideredirect.geometry('200x70+250+250')

    def show(self):
        self.root.mainloop()

if __name__ == "__main__":
    user_toplevel = UToplevel()
    user_toplevel.show()
