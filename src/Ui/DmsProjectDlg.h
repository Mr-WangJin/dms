#pragma once


#include "ui_DmsProjectDlg.h"


class DMSProjectDlg : public QDialog
{
    Q_OBJECT
public:
    DMSProjectDlg(QWidget* parent = nullptr);
    ~DMSProjectDlg();

private:
    void on_tBtnOpen_clicked();
    void on_tBtnNew_clicked();


private:
    Ui_DmsProjectDlg ui;


};


