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
        QMessageBox::information(nullptr, QStringLiteral("��ʾ"), e.what());

    }
    catch (...)
    {
        QMessageBox::information(nullptr, QStringLiteral("��ʾ"), QStringLiteral("δ֪�쳣"));
    }
}

