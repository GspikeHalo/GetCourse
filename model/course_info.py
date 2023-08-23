# model/course_info.py
# 该模块中包含了课程信息类，用于储存一节课的所有信息

class CourseInfo:
    """
    该类为一节课中包含的所有信息
    """
    def __init__(self, list_of_course_info):
        self.code = list_of_course_info[0]
        self.type = list_of_course_info[1]
        self.sec = list_of_course_info[2]
        self.units = list_of_course_info[3]
        self.instructor = list_of_course_info[4]
        self.time = list_of_course_info[5]
        self.place = list_of_course_info[6]
        self.final = list_of_course_info[7]
        self.max = list_of_course_info[8]
        self.enr = list_of_course_info[9]
        self.wl = list_of_course_info[10]
        self.req = list_of_course_info[11]
        self.nor = list_of_course_info[12]
        self.rstr = list_of_course_info[13]
        self.textbooks = list_of_course_info[14]
        self.web = list_of_course_info[15]
        self.status = list_of_course_info[16]