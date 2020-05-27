# 上下文类
from dal.dmsDatabase import *


class DMSContext(object):
    project = None
    BUTTON_NORMAL_HEIGHT = 40
    TOOLBAR_HEIGHT = 32
    TEXT_TABLE_HEADER_SIZE = 14
    """docstring for DMSContext"""

    def __init__(self):
        self.project = None

    # 设置工程
    def setProject(self, project):
        self.project = project

    def getProject(self):
        return self.project


# 上下文全局变量
glb_dmsContext = DMSContext()


def dmsProject():
    return glb_dmsContext.getProject()


def dmsDatabase():
    return glb_dmsContext.getProject().dmsDatabase


# 判断工程是否为空
def isProjectNull():
    if glb_dmsContext.getProject() is None:
        return True
    return False
