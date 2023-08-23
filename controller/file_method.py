# controller/file_method.py
# 改模块包含了文件方法类，该类中包含了所有与文件更改相关的方法

import time
from model.course_info import CourseInfo


LOGPATH = "./resource/log.txt"  # log文档的储存位置
CHROMEDRIVERPATH = "./resource/chromedriver.txt"  # chromedriver.exe文件的储存位置
SENDEMAIL = "./resource/email.txt"  # sender的邮箱信息所储存的位置


class FileMethod:
    """
    该类包含与文件相关的所有方法
    """

    @staticmethod
    def create_log_base_info(major: str, course_code: str) -> None:
        """
        该方法将用户想要查找的课程的基本信息存储进log文件中
        :param major: 用户想选的课程专业
        :param course_code: 用户想选的课程编号
        :return: None
        """
        with open(LOGPATH, "a", encoding = "utf-8") as file:
            content = "COURSE INFO: {} {}\n".format(major, course_code)
            file.write(content)

    @staticmethod
    def create_log_course_info(result: list[CourseInfo]) -> None:
        """
        该方法将用户想要查找的课程的当前时间的信息储存进入log文档中
        :param result: 课程信息列表
        :return: None
        """
        with open(LOGPATH, "a", encoding = "utf-8") as file:
            file.write(time.ctime() + "\n")
            for row in result:
                content = "Course Code: {}, Course Type: {}, Max: {}, Cur: {}, Status: {}\n".format(
                    row.code, row.type, row.max, row.enr, row.status)
                file.write(content)
            file.write("\n")

    @staticmethod
    def get_log_content() -> str:
        """
        该方法将获取log文档中的内容
        :return: log文档中的内容
        """
        with open(LOGPATH, "r") as file:
            content = file.read()
        return content

    @staticmethod
    def empty_log_content() -> None:
        """
        该方法将清空log文档中的内容
        :return: None
        """
        with open(LOGPATH, "w") as file:
            file.write("")

    @staticmethod
    def set_chrome_driver_path(chrome_driver_path: str) -> None:
        """
        该方法将chromedriver.exe文件的绝对地址保存到chromedriver文档中
        :param chrome_driver_path: chromedriver.exe的绝对地址
        :return: None
        """
        with open(CHROMEDRIVERPATH, "w") as file:
            file.write(chrome_driver_path)

    @staticmethod
    def get_chrome_driver_path() -> str:
        """
        该方法将获取chromedriver.exe文件的绝对地址
        :return: chromedriver.exe文件的绝对地址
        """
        with open(CHROMEDRIVERPATH, "r") as file:
            content = file.read()
        return content

    @staticmethod
    def set_sender(email_type: str, account: str, password: str) -> None:
        """
        该方法将邮件的发送者的信息保存到email.txt文档中
        :param email_type: 发送者的邮箱类型
        :param account: 发送者的邮箱账号
        :param password: 发送者的SMTP密码
        :return: None
        """
        with open(SENDEMAIL, "w") as file:
            content = "{} {} {}".format(email_type, account, password)
            file.write(content)

    @staticmethod
    def get_sender() -> tuple:
        """
        该方法将获取发送者的邮箱的基本信息，包括邮箱类型，账号和密码
        :return: 邮箱类型，账号和密码
        """
        with open(SENDEMAIL, "r") as file:
            content = file.read()
        result = content.split()
        return result[0], result[1], result[2]

    @staticmethod
    def empty_sender() -> None:
        """
        该方法将清空email.txt文档中的内容
        :return: None
        """
        with open(SENDEMAIL, "w") as file:
            file.write("")
