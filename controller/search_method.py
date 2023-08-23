# controller/search_method.py
# 改模块包含了搜索方法类，该类中的所有方法与html搜索相关

import subprocess
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .file_method import FileMethod
from model.course_info import CourseInfo


UCIURL = "https://www.reg.uci.edu/perl/WebSoc" #UCI当前的选课网址


class SearchMethod:
    """
    该类包含所有与html搜索相关的方法
    """

    @staticmethod
    def get_course_html_content(dept: str, course_num: str) -> str:
        """
        该方法将访问用户想要查询的课程界面 并返回课程界面的html源码
        :param dept: 目标专业
        :param course_num: 目标课号
        :return: 课程界面的html源码
        """
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        chromedriver_path = FileMethod.get_chrome_driver_path()
        service = subprocess.Popen([chromedriver_path, '--port=4444'],
                                   creationflags = subprocess.CREATE_NO_WINDOW)
        driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4444', options = options)
        driver.get(UCIURL)

        select_department = Select(driver.find_element(By.NAME, "Dept"))
        select_department.select_by_visible_text(dept)  # 在专业选择中选择专业
        course_number_input = driver.find_element(By.NAME, "CourseNum")
        course_number_input.send_keys(course_num)  # 在课号中输入课号
        submit_button = driver.find_element(By.NAME, "Submit")
        submit_button.click()  # 进入已选择的课程界面
        driver.implicitly_wait(10)
        html_content = driver.page_source

        driver.quit()
        service.terminate()
        return html_content

    @staticmethod
    def get_course_info(course_page_html: str) -> list[CourseInfo]:
        """
        该方法接受一个网页（课程界面）的html源码，并将已有课程的信息储存为数组返回
        :param course_page_html: 网站的html源码
        :return: 课程信息
        """
        soup = BeautifulSoup(course_page_html, "html.parser")
        rows = soup.find_all("tr")
        result = []
        for row in rows:
            cells = row.find_all("td")
            attributes = [cell['bgcolor'] if cell.has_attr('bgcolor') else None for cell in cells]
            if "#D5E5FF" in attributes or "#DDEEFF" in attributes:
                data = [cell.get_text() for cell in cells]
                information = CourseInfo(data)
                result.append(information)
        return result
