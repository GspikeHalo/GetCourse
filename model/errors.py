# model/errors.py
# 该模块包含该程序可能出现的所有错误，包括与文件相关的错误，与邮箱相关的错误，还有与html搜索相关的错误

class Error000(Exception):
    """邮箱相关的错误"""
    pass


class Error100(Exception):
    """
    文件相关的错误
    """
    pass


class Error200(Exception):
    """
    html搜索相关的错误
    """
    pass


class Error001(Error000):
    """
    当服务器拒绝登录尝试时会出现该错误，例如登录邮箱的用户名或者密码错误（测试用）
    """

    def __init__(self):
        error_msg = "认证错误：请检查用户名和密码"
        super().__init__(error_msg)


class Error002(Error000):
    """
    当服务器不接受收件人地址时会出现该错误，例如收件人的邮箱填写错误
    """

    def __init__(self):
        error_msg = "认证错误：请检查邮箱"
        super().__init__(error_msg)


class Error003(Error000):
    """
    当发送邮件时出现错误，但是不知道错误的具体类型时出现该错误
    """

    def __init__(self, msg):
        error_msg = "发送邮件时出现错误{}".format(msg)
        super().__init__(error_msg)


class Error101(Error100):
    """
    当无法找到文件时出现该错误
    """

    def __init__(self):
        error_msg = "无法找到log文件"
        super().__init__(error_msg)


class Error102(Error100):
    """
    当打开文件出现异常时出现该错误
    """

    def __init__(self, msg):
        error_msg = "文件打开异常:{}".format(msg)
        super().__init__(error_msg)


class Error201(Error200):
    """
    当在html中没有找到想要的元素时出现该错误
    """

    def __init__(self):
        error_msg = "未找到需要元素"
        super().__init__(error_msg)


class Error202(Error200):
    """
    当执行搜索html时间过长时出现该错误
    """

    def __init__(self):
        error_msg = "操作超时"
        super().__init__(error_msg)


class Error203(Error200):
    """
    当访问html中不存在的元素或者属性时会返回None，如果想要进一步访问，则会出现该错误
    """

    def __init__(self, msg):
        error_msg = "属性错误:{}".format(msg)
        super().__init__(error_msg)


class Error204(Error200):
    """
    当BS出现其他错误时，会出现该错误
    """

    def __init__(self, msg):
        error_msg = "BS出现错误：{}".format(msg)
        super().__init__(error_msg)
