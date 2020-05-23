# 上下文类

class DMSContext(object):
    project = None

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
    return  glb_dmsContext.getProject().dmsDatabase
