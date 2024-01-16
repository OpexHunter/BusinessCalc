# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupUserEditUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QWidget)
from . import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(563, 108)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.b_save = QPushButton(Dialog)
        self.b_save.setObjectName(u"b_save")
        self.b_save.setGeometry(QRect(460, 80, 91, 24))
        self.b_save.setStyleSheet(u"QPushButton {\n"
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 541, 61))
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"	background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 2px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(190, 30, 331, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.can_see = QCheckBox(self.layoutWidget)
        self.can_see.setObjectName(u"can_see")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.can_see.sizePolicy().hasHeightForWidth())
        self.can_see.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.can_see)

        self.can_report = QCheckBox(self.layoutWidget)
        self.can_report.setObjectName(u"can_report")
        sizePolicy.setHeightForWidth(self.can_report.sizePolicy().hasHeightForWidth())
        self.can_report.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.can_report)

        self.admin = QCheckBox(self.layoutWidget)
        self.admin.setObjectName(u"admin")
        sizePolicy.setHeightForWidth(self.admin.sizePolicy().hasHeightForWidth())
        self.admin.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.admin)

        self.l_login = QLabel(self.frame)
        self.l_login.setObjectName(u"l_login")
        self.l_login.setGeometry(QRect(10, 30, 181, 20))
        self.l_login.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 5, 541, 21))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"	margin-left: 2px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.l_fio_email = QLabel(Dialog)
        self.l_fio_email.setObjectName(u"l_fio_email")
        self.l_fio_email.setGeometry(QRect(10, 80, 441, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.b_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.can_see.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.can_report.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0451\u0442\u043e\u0432", None))
        self.admin.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u043c\u0438\u043d", None))
        self.l_login.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435 \u043d\u0430\u0439\u0434\u0435\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0430\u0432\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.l_fio_email.setText(QCoreApplication.translate("Dialog", u"\u0424.\u0418.\u041e | e-mail: ...", None))
    # retranslateUi

