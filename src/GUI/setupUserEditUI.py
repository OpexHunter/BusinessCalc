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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(563, 108)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 80, 91, 24))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
"    background-color: rgb(225,225,225);\n"
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
        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.checkBox_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 171, 20))
        self.label.setStyleSheet(u"QLabel {\n"
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
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 441, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0430\u0432 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043e\u0442\u0447\u0451\u0442\u043e\u0432", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u0410\u0434\u043c\u0438\u043d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0430\u0432\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0410\u0431\u043e\u0431\u0430 \u0410\u0431\u043e\u0431\u043e\u0432\u0438\u0447 | e-mail: aboba@mail.ru", None))
    # retranslateUi

