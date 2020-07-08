#include "stdafx.h"
#include "Ui/DmsMainWin.h"


int main(int argc, char** argv)
{
    QApplication a(argc, argv);

    try {
        DmsMainWin w;
        w.show();

        return a.exec();
    }
    catch (std::exception & e)
    {
        QMessageBox::information(nullptr, QStringLiteral("提示"), e.what());

    }
    catch (...)
    {
        QMessageBox::information(nullptr, QStringLiteral("提示"), QStringLiteral("未知异常"));
    }
}

