# view/main_view.py
# 改模块为view界面的主体设计

from .dialog import *
import tkinter.messagebox
from model.department_info import Department
from tkinter import ttk
from controller.controller import Controller


class MainView:
    """
    该类为程序的主要界面
    """

    def __init__(self):
        self.master = self.set_root()
        self.controller = Controller()
        self.body(self.master)

    def set_root(self):
        root = tk.Tk()
        root.geometry("565x400")
        root.title("Get Course")
        root.iconbitmap('./resource/uci.ico')
        root.resizable(False, False)
        return root

    def main_board_run(self):
        self.master.mainloop()

    def body(self, master):
        self.main_menu = tk.Menu(master)
        self.set_main_menu(master)
        self.master.config(menu = self.main_menu)

        self.info_frame = tk.Frame(master)
        self.info_frame.grid(row = 0, sticky = tk.N)
        self.info_frame_set(self.info_frame)

        self.process_frame = tk.Frame(master)
        self.process_frame.grid(row = 1, sticky = tk.S)
        self.process_frame_set(self.process_frame)

    def set_main_menu(self, master):
        self.email_menu = tk.Menu(self.main_menu, tearoff = False)
        self.main_menu.add_cascade(label = "邮箱", menu = self.email_menu)
        self.email_menu.add_command(label = "设置接收邮箱",
                                    command = lambda: self.change_recv_email(master))
        self.email_menu.add_command(label = "设置发送邮箱",
                                    command = lambda: self.change_send_email(master))
        self.email_menu.add_command(label = "清空发送邮箱", command = self.empty_sender_email)
        self.main_menu.add_command(label = "ChromeDrive",
                                   command = lambda: self.set_chrome_driver(master))
        self.main_menu.add_command(label = "清空日志", command = self.empty_log_file)

    def info_frame_set(self, master):
        self.now_email_label = tk.Label(master, text = "Email:")
        self.now_email_label.grid(row = 0, column = 0, sticky = tk.E)
        self.now_email_label = tk.Label(master, text = "")
        self.now_email_label.grid(row = 0, column = 1, sticky = tk.W)

        self.major_label = tk.Label(master, text = "Department:")
        self.major_label.grid(row = 1, column = 0, sticky = tk.E)
        self.major_combobox = ttk.Combobox(master, values = Department.department, width = 40)
        self.major_combobox.grid(row = 1, column = 1, sticky = tk.W)

        self.course_code_label = tk.Label(master, text = "Course Num:")
        self.course_code_label.grid(row = 2, column = 0, sticky = tk.E)
        self.course_code_entry = tk.Entry(master, width = 42)
        self.course_code_entry.grid(row = 2, column = 1, sticky = tk.W)

        self.make_sure_button = tk.Button(master, text = "确定", width = 10,
                                          command = self.start_search)
        self.make_sure_button.grid(row = 1, column = 2, padx = 10)

        self.cancel_button = tk.Button(master, text = "重置", width = 10,
                                       command = self.reset_search)
        self.cancel_button.grid(row = 2, column = 2)

    def process_frame_set(self, master):
        process_text = ("现在以运行：{}".format(self.controller.run_times))
        self.process_lable = tk.Label(master, text = process_text)
        self.process_lable.pack(expand = tk.TRUE, fill = tk.BOTH)

        self.log_text = tk.Text(master, wrap = "word")
        self.log_text.pack(expand = tk.TRUE, fill = tk.BOTH)
        self.set_log_text()

    def set_log_text(self):
        try:
            content = self.controller.get_log()
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.INSERT, content)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def change_send_email(self, master):
        try:
            self.email_send_dia = SendEmailAskDialog(master)
            result = self.email_send_dia.result
            if result and result[0] and result[1] and result[2]:
                self.controller.set_send_email(result)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def change_recv_email(self, master):
        try:
            self.email_recv_dia = RecvEmailAskDialog(master)
            result = self.email_recv_dia.result
            if result:
                self.controller.test_email(result)
                self.now_email_label.config(text = result)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def empty_sender_email(self):
        try:
            self.controller.empty_send_email()
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def set_chrome_driver(self, master):
        try:
            self.chromedriver_path_dia = PathAskDialog(master)
            result = self.chromedriver_path_dia.result
            if result:
                self.controller.set_chromedriver(result)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def empty_log_file(self):
        try:
            self.controller.empty_log()
            self.set_log_text()
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def start_search(self):
        try:
            self.controller.start_search(email = self.email_recv_dia.result,
                                         department = self.major_combobox.get(),
                                         code = self.course_code_entry.get())
            process_times = "现在以运行：{}".format(self.controller.run_times)
            self.process_lable.config(text = process_times)
            self.set_log_text()
            self.master.after(3600000, self.start_search)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))

    def reset_search(self):
        try:
            self.major_combobox.current(0)
            self.course_code_entry.delete(0, tk.END)
        except Exception as e:
            tkinter.messagebox.showerror("ERROR", str(e))
