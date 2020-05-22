# 上下文类


class DMSContext(object):
    project = None

    """docstring for DMSContext"""

    def __init__(self):
        self.project = None

    # 设置工程
    def setProject(self, project):
        self.project = project


# 上下文全局变量
dms_context = DMSContext()
