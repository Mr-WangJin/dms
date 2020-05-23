import sys
from PyQt5.QtWidgets import QApplication
from ui.dmsMainWin import DMSMainWin


class DMSApplication(QApplication):
    def __init__(self, argv):
        super(DMSApplication, self).__init__(argv)
        pass

    def notify(self, QObject, QEvent):  # real signature unknown; restored from __doc__
        try:
            return super(DMSApplication, self).notify(QObject, QEvent)
        except BaseException as err:
            print(err)
        except:
            print("Unexpected error:", sys.exc_info()[0])


if __name__ == '__main__':
    app = DMSApplication(sys.argv)

    main_form = DMSMainWin()
    main_form.show()
    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
