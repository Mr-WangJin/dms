# encoding: utf-8

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from ui.dmsMainWin import DMSMainWin
import traceback


class DMSApplication(QApplication):
    def __init__(self, argv):
        super(DMSApplication, self).__init__(argv)
        pass

    def notify(self, QObject, QEvent):  # real signature unknown; restored from __doc__
        try:
            super(DMSApplication, self).notify(QObject, QEvent)
        except BaseException as err:
            print(err)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            pass
        finally:
            pass

        return False


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message: ", tb)
    QtWidgets.QApplication.quit()
    # or QtWidgets.QApplication.exit(0)


if __name__ == '__main__':
    # 设置捕获异常
    sys.excepthook = excepthook

    app = DMSApplication(sys.argv)

    main_form = DMSMainWin()
    main_form.showMaximized()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
