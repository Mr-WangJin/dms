#include "stdafx.h"
#include "DmsMainWin.h"
#include "DmsProjectDlg.h"


DmsMainWin::DmsMainWin(QWidget* parent /*= nullptr*/)
    : QMainWindow(parent)
{
    if (!this->showProjectUi())
        return;

    ui.setupUi(this);

}

DmsMainWin::~DmsMainWin()
{
}

bool DmsMainWin::showProjectUi()
{
    DMSProjectDlg projectDlg;

    projectDlg.exec();

    return true;
}

