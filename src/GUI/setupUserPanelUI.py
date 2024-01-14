# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupUserPanelUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QTableView, QWidget)
from . import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(881, 495)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.UserTable = QTableView(Dialog)
        self.UserTable.setObjectName(u"UserTable")
        self.UserTable.setGeometry(QRect(0, 0, 881, 451))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(450, 460, 421, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.refresh = QPushButton(self.layoutWidget)
        self.refresh.setObjectName(u"refresh")
        self.refresh.setMinimumSize(QSize(0, 25))
        self.refresh.setMaximumSize(QSize(95, 16777215))
        self.refresh.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_2.addWidget(self.refresh)

        self.commit = QPushButton(self.layoutWidget)
        self.commit.setObjectName(u"commit")
        self.commit.setMinimumSize(QSize(0, 25))
        self.commit.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_2.addWidget(self.commit)

        self.remove = QPushButton(self.layoutWidget)
        self.remove.setObjectName(u"remove")
        self.remove.setMinimumSize(QSize(155, 25))
        self.remove.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(225,225,225);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(235,235,235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(225,225,225);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")

        self.horizontalLayout_2.addWidget(self.remove)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0430\u0432\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.refresh.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.commit.setText(QCoreApplication.translate("Dialog", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u043e\u0441\u0442\u0443\u043f", None))
        self.remove.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi

