#pragma once

#include "ui_DmsMainWin.h"

class DmsMainWin : public QMainWindow
{
public:
    DmsMainWin(QWidget* parent = nullptr);
    ~DmsMainWin();


private:
    bool showProjectUi();

private:
    Ui_DmsMainWin ui;

};

