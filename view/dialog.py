# view/dialog.py
# 该模块中包含了view中的定制对话框

import tkinter as tk
from tkinter import simpledialog


class SendEmailAskDialog(simpledialog.Dialog):
    """
    该类是对询问sender邮件的对话框的定制
    该对话框的结果为一个包含三个元素的tuple，分别是邮箱类型，邮箱账号和邮箱密码
    """

    def body(self, master):
        self.selected = tk.StringVar()
        self.option1 = tk.Radiobutton(master, text = "Gmail", variable = self.selected,
                                      value = "Option1")
        self.option2 = tk.Radiobutton(master, text = "163", variable = self.selected,
                                      value = "Option2")
        self.option1.grid(row = 0, column = 0)
        self.option2.grid(row = 0, column = 1)

        self.title("Email")
        tk.Label(master, text = "邮箱账号：").grid(row = 2, column = 0)
        self.entry_email = tk.Entry(master, width = 25)
        self.entry_email.grid(row = 2, column = 1)

        tk.Label(master, text = "邮箱SMTP密码：").grid(row = 3, column = 0)
        self.entry_password = tk.Entry(master, width = 25)
        self.entry_password.grid(row = 3, column = 1)
        return self.entry_email

    def apply(self):
        self.result = (self.selected.get(), self.entry_email.get(), self.entry_password.get())


class RecvEmailAskDialog(simpledialog.Dialog):
    """
    该类是对询问recver邮箱的对话框
    该对话框的结果为recver的邮箱账号
    """

    def body(self, master):
        self.title("Email")
        tk.Label(master, text = "邮箱账号：").grid(row = 0, column = 0)
        self.entry_email = tk.Entry(master, width = 25)
        self.entry_email.grid(row = 0, column = 1)
        return self.entry_email

    def apply(self):
        self.result = self.entry_email.get()


class PathAskDialog(simpledialog.Dialog):
    """
    该类是对询问chromedriver.exe地址的对话框
    对话框的结果为chromedriver.exe的绝对地址
    """

    def body(self, master):
        self.title("Chrome Driver Address")
        tk.Label(master, text = "请输入Chrome Driver地址").grid(row = 0)
        self.entry = tk.Entry(master, width = 30)
        self.entry.grid(row = 0, column = 1)
        tk.Label(master, text = '复制当前文件夹地址 + "\\resource\chromedriver.exe"').grid(row = 1,
                                                                                           column = 0,
                                                                                           columnspan = 2,
                                                                                           sticky = tk.E + tk.W)
        return self.entry

    def apply(self):
        self.result = self.entry.get()
