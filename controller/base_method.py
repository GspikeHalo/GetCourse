# controller/base_method.py

import smtplib
from email.mime.text import MIMEText
from model.course_info import CourseInfo

from .search_method import SearchMethod, FileMethod


class BaseMethod:
    """
    该类包含一些最基本的方法
    """
    @staticmethod
    def judge_status(course_info: list[CourseInfo]) -> bool:
        """
        判断当前时间课程中是否有空位
        :param course_info: 当前课程信息
        :return: 是否有空位
        """
        want_status = "OPEN"
        for row in course_info:
            if row.status == want_status:
                return True
        return False

    @staticmethod
    def send_email(recv_account: str, subject: str, body: str) -> None:
        """
        为用户发送邮件
        :param recv_account: 接收者的邮箱账号
        :param subject: 课程的专业
        :param body: 课程的编号
        :return: None
        """
        email_type, host_account, host_password = FileMethod.get_sender()
        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = host_account
        msg["To"] = recv_account
        server = None

        if email_type == "Option1":
            server = smtplib.SMTP("smtp.gmail.com", 587)
        elif email_type == "Option2":
            server = smtplib.SMTP("smtp.163.com", 25)

        server.starttls()
        server.login(host_account, host_password)
        server.send_message(msg)




