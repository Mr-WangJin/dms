# 上下文类
# from bll.dmsProject import DMSProject
from dal.dmsDatabase import *

# 上下文
class DMSContext(object):
    project = None
    BUTTON_NORMAL_HEIGHT = 32
    TOOLBAR_HEIGHT = 32
    TEXT_TABLE_HEADER_SIZE = 14
    IS_DEBUG = True
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


def dmsDatabase() -> DMSDatabase:
    return glb_dmsContext.getProject().dmsDatabase


# 判断工程是否为空
def isProjectNull():
    if glb_dmsContext.getProject() is None:
        return True
    return False


def isDebug() -> bool:
    return True
