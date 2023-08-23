# controller/controller.py
# 改模块包含程序的控制器类，类中的方法将view和model连接起来

import smtplib
from .file_method import FileMethod
from .search_method import SearchMethod
from .base_method import BaseMethod
from model.errors import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Controller:
    """
    该类为程序的控制器，类中的方法将view与model的方法进行连接
    """

    def __init__(self):
        self.run_times = 0  # 运行次数

    def start_search(self, email: str, department: str, code: str) -> None:
        """
        该方法为开始对指定信息的搜索，并将搜索结果发送给用户的方法
        :param email: 用户邮箱
        :param department: 用户想要查询的专业
        :param code: 用户想要查询的课号
        :return: None
        """
        self.run_times += 1
        self.test_create_log_base_info(department, code)
        html_content = self.test_get_course_html_content(department, code)
        courses_info = self.test_get_course_info(html_content)
        if BaseMethod.judge_status(courses_info):
            self.send_course_prompt(email, department, code)
        self.test_create_log_course_info(courses_info)

    @staticmethod
    def get_log():
        """
        该方法将获取log文档中的内容，同时检测错误
        :return: None
        """
        try:
            return FileMethod.get_log_content()
        except FileNotFoundError:
            raise Error101
        except Exception:
            raise Error102

    @staticmethod
    def empty_log():
        """
        该方法将清空log文档中的内容，同时检测错误
        :return:
        """
        try:
            FileMethod.empty_log_content()
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))

    @staticmethod
    def set_chromedriver(chrome_driver_path: str) -> None:
        """
        该方法将chromedriver.exe的地址储存进对应的文件，同时检测错误
        :param chrome_driver_path: chromedriver.exe的地址
        :return: None
        """
        try:
            FileMethod.set_chrome_driver_path(chrome_driver_path)
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))

    @staticmethod
    def set_send_email(email_info: tuple) -> None:
        """
        该方法将sender的邮箱信息储存进对应的文件，同时检查错误
        :param email_info: sender邮箱的基本信息，包含邮箱类型，账号和STML密码
        :return: None
        """
        try:
            email_type, account, password = email_info
            FileMethod.set_sender(email_type, account, password)
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))

    @staticmethod
    def empty_send_email() -> None:
        """
        该方法将清空sender的邮箱信息，同时检查错误
        :return: None
        """
        try:
            FileMethod.empty_sender()
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))

    @staticmethod
    def test_email(recv_account: str) -> None:
        """
        该方法将测试recver的邮箱是否可以接收到邮件
        :param recv_account: 接收者的邮箱账号
        :return: None
        """
        try:
            subject = "测试邮箱连接"
            body = "邮箱连接成功"
            BaseMethod.send_email(recv_account, subject, body)
        except smtplib.SMTPAuthenticationError:
            raise Error001
        except smtplib.SMTPRecipientsRefused:
            raise Error002
        except smtplib.SMTPException as e:
            raise Error003(e)

    @staticmethod
    def send_course_prompt(recv_account: str, major: str, code: str) -> None:
        """
        该方法将给用户发送邮件，邮件内容为想要的课已有位置
        :param recv_account: 用户的邮箱账号
        :param major: 用户想要选取的专业
        :param code: 用户想要选取的课号
        :return: None
        """
        try:
            subject = "你想要的课{} {}有闲置位置！".format(major, code)
            body = "你想要的课{} {}有闲置位置！".format(major, code)
            BaseMethod.send_email(recv_account, subject, body)
        except smtplib.SMTPAuthenticationError:
            raise Error001
        except smtplib.SMTPRecipientsRefused:
            raise Error002
        except smtplib.SMTPException as e:
            raise Error003(e)

    @staticmethod
    def test_create_log_base_info(department: str, code: str) -> None:
        """
        该方法将检测create_log_base_info方法是否有错误
        :param department: 用户想要选取的专业
        :param code: 用户想要选取的课号
        :return: None
        """
        try:
            FileMethod.create_log_base_info(department, code)
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))

    @staticmethod
    def test_get_course_html_content(department: str, code: str) -> str:
        """
        该方法将检测get_course_html_content方法是否有错误
        :param department: 用户想要选取的专业
        :param code: 用户想要选取的课号
        :return: 选课界面的html源码
        """
        try:
            return SearchMethod.get_course_html_content(department, code)
        except NoSuchElementException:
            raise Error201
        except TimeoutException:
            raise Error202

    @staticmethod
    def test_get_course_info(html_content: str) -> list:
        """
        该方法将检测get_course_info方法是否有错误
        :param html_content: 选课界面的html源码
        :return: 课程信息
        """
        try:
            return SearchMethod.get_course_info(html_content)
        except AttributeError as e:
            raise Error203(e)
        except Exception as e:
            raise Error204(e)

    @staticmethod
    def test_create_log_course_info(courses_info: list) -> None:
        """
        该方法将检测create_log_course_info方法是否有错误
        :param courses_info: 课程信息
        :return: None
        """
        try:
            FileMethod.create_log_course_info(courses_info)
        except FileNotFoundError:
            raise Error101
        except Exception as e:
            raise Error102(str(e))
