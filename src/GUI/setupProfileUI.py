# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupProfileUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from . import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 320)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame_help = QFrame(Dialog)
        self.frame_help.setObjectName(u"frame_help")
        self.frame_help.setGeometry(QRect(10, 10, 581, 301))
        self.frame_help.setStyleSheet(u"QFrame#frame_help {\n"
"	background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.frame_help.setFrameShape(QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QFrame.Raised)
        self.login = QFrame(self.frame_help)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(30, 140, 241, 91))
        self.login.setStyleSheet(u"QFrame#login {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 221, 76))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.l_log = QLineEdit(self.layoutWidget)
        self.l_log.setObjectName(u"l_log")
        self.l_log.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.l_log)

        self.l_pass = QLineEdit(self.layoutWidget)
        self.l_pass.setObjectName(u"l_pass")
        self.l_pass.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")
        self.l_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.l_pass)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_button = QPushButton(self.layoutWidget)
        self.l_button.setObjectName(u"l_button")
        self.l_button.setMinimumSize(QSize(0, 20))
        self.l_button.setMaximumSize(QSize(16777215, 16777215))
        self.l_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.l_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.reg = QFrame(self.frame_help)
        self.reg.setObjectName(u"reg")
        self.reg.setGeometry(QRect(290, 140, 241, 141))
        self.reg.setStyleSheet(u"QFrame#reg {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.reg.setFrameShape(QFrame.StyledPanel)
        self.reg.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.reg)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 221, 128))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.r_fio = QLineEdit(self.layoutWidget1)
        self.r_fio.setObjectName(u"r_fio")
        self.r_fio.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.r_fio)

        self.r_log = QLineEdit(self.layoutWidget1)
        self.r_log.setObjectName(u"r_log")
        self.r_log.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.r_log)

        self.r_pass = QLineEdit(self.layoutWidget1)
        self.r_pass.setObjectName(u"r_pass")
        self.r_pass.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")
        self.r_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.r_pass)

        self.r_email = QLineEdit(self.layoutWidget1)
        self.r_email.setObjectName(u"r_email")
        self.r_email.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.r_email)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.r_button = QPushButton(self.layoutWidget1)
        self.r_button.setObjectName(u"r_button")
        self.r_button.setMinimumSize(QSize(0, 20))
        self.r_button.setMaximumSize(QSize(16777215, 16777215))
        self.r_button.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.r_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.user = QFrame(self.frame_help)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(30, 0, 501, 91))
        self.user.setStyleSheet(u"QFrame#user {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.user.setFrameShape(QFrame.StyledPanel)
        self.user.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.user)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 32, 481, 41))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.i_name = QLabel(self.layoutWidget2)
        self.i_name.setObjectName(u"i_name")
        self.i_name.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")

        self.verticalLayout_3.addWidget(self.i_name)

        self.i_access = QLabel(self.layoutWidget2)
        self.i_access.setObjectName(u"i_access")
        self.i_access.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")

        self.verticalLayout_3.addWidget(self.i_access)

        self.Name_3 = QLabel(self.user)
        self.Name_3.setObjectName(u"Name_3")
        self.Name_3.setGeometry(QRect(10, 10, 551, 19))
        self.Name_3.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"	margin-left: 2px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.info = QFrame(self.frame_help)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(30, 100, 501, 31))
        self.info.setStyleSheet(u"QFrame#info {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.info.setFrameShape(QFrame.StyledPanel)
        self.info.setFrameShadow(QFrame.Raised)
        self.Name_4 = QLabel(self.info)
        self.Name_4.setObjectName(u"Name_4")
        self.Name_4.setGeometry(QRect(0, 0, 501, 31))
        self.Name_4.setStyleSheet(u"QLabel {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.Name_4.setAlignment(Qt.AlignCenter)
        self.load_1 = QLabel(self.frame_help)
        self.load_1.setObjectName(u"load_1")
        self.load_1.setGeometry(QRect(28, 229, 241, 21))
        self.load_1.setAlignment(Qt.AlignCenter)
        self.load_2 = QLabel(self.frame_help)
        self.load_2.setObjectName(u"load_2")
        self.load_2.setGeometry(QRect(290, 280, 241, 21))
        self.load_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.l_log.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.l_pass.setText("")
        self.l_pass.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.l_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.r_fio.setText("")
        self.r_fio.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0424.\u0418.\u041e.", None))
        self.r_log.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.r_pass.setText("")
        self.r_pass.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.r_email.setPlaceholderText(QCoreApplication.translate("Dialog", u"e-mail", None))
        self.r_button.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.i_name.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c: \u043d\u0435 \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u043e\u0432\u0430\u043d", None))
        self.i_access.setText(QCoreApplication.translate("Dialog", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u0430: \u0434\u043e\u0441\u0442\u0443\u043f \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.Name_3.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.Name_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434 / \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.load_1.setText("")
        self.load_2.setText("")
    # retranslateUi

