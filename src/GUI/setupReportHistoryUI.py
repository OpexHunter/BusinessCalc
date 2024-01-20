# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupReportHistoryUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QWidget)
from . import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(881, 498)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.SeeReport = QPushButton(Dialog)
        self.SeeReport.setObjectName(u"SeeReport")
        self.SeeReport.setGeometry(QRect(750, 460, 121, 31))
        self.SeeReport.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,255);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")
        self.HistoryTable = QTableView(Dialog)
        self.HistoryTable.setObjectName(u"HistoryTable")
        self.HistoryTable.setGeometry(QRect(0, 0, 881, 451))
        self.refresh = QPushButton(Dialog)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setGeometry(QRect(650, 460, 91, 31))
        self.refresh.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,255);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043e\u0442\u0447\u0451\u0442\u043e\u0432", None))
        self.SeeReport.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043e\u0442\u0447\u0451\u0442\u0430", None))
        self.refresh.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

