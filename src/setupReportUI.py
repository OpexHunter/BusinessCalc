# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupReportUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGraphicsView,
    QLabel, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)
import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(741, 422)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.res = QFrame(Dialog)
        self.res.setObjectName(u"res")
        self.res.setGeometry(QRect(10, 10, 431, 391))
        self.res.setStyleSheet(u"QFrame#res {\n"
"	background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.res.setFrameShape(QFrame.StyledPanel)
        self.res.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.res)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 331, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")
        self.res_osn = QFrame(self.res)
        self.res_osn.setObjectName(u"res_osn")
        self.res_osn.setGeometry(QRect(0, 40, 401, 141))
        self.res_osn.setStyleSheet(u"QFrame#res_osn {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(238,238,238);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(245,245,245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(238,238,238);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")
        self.res_osn.setFrameShape(QFrame.StyledPanel)
        self.res_osn.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.res_osn)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 331, 101))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 0, 0, 0)
        self.rep1 = QLabel(self.widget)
        self.rep1.setObjectName(u"rep1")

        self.verticalLayout.addWidget(self.rep1)

        self.rep2 = QLabel(self.widget)
        self.rep2.setObjectName(u"rep2")

        self.verticalLayout.addWidget(self.rep2)

        self.rep3 = QLabel(self.widget)
        self.rep3.setObjectName(u"rep3")

        self.verticalLayout.addWidget(self.rep3)

        self.rep4 = QLabel(self.widget)
        self.rep4.setObjectName(u"rep4")

        self.verticalLayout.addWidget(self.rep4)

        self.rep5 = QLabel(self.widget)
        self.rep5.setObjectName(u"rep5")

        self.verticalLayout.addWidget(self.rep5)

        self.label_2 = QLabel(self.res_osn)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 321, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.res_dop = QFrame(self.res)
        self.res_dop.setObjectName(u"res_dop")
        self.res_dop.setGeometry(QRect(0, 210, 401, 151))
        self.res_dop.setStyleSheet(u"QFrame#res_dop {\n"
"	background-color: rgba(0, 0, 0, 0.01);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(238,238,238);\n"
"    border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(245,245,245);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(238,238,238);\n"
"    color: rgba(0,0,0,0.4)\n"
"}")
        self.res_dop.setFrameShape(QFrame.StyledPanel)
        self.res_dop.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.res_dop)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 321, 16))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.textBrowser = QTextBrowser(self.res_dop)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 30, 371, 111))
        self.textBrowser.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(0, 0, 0, 0.00);\n"
"   border: 0px solid rgba(0, 0, 0, 0); border-radius: 0px;\n"
"}")
        self.widget1 = QWidget(Dialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(470, 10, 258, 392))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.widget1)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.graphicsView_2 = QGraphicsView(self.widget1)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_2.addWidget(self.graphicsView_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043e\u0442\u0447\u0451\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0436\u0438\u0434\u0430\u0435\u043c\u044b\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.rep1.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043e\u043a\u0443\u043f\u0430\u0435\u043c\u043e\u0441\u0442\u0438:", None))
        self.rep2.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b:", None))
        self.rep3.setText(QCoreApplication.translate("Dialog", u"\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b:", None))
        self.rep4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0445\u043e\u0434 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d\u0430:", None))
        self.rep5.setText(QCoreApplication.translate("Dialog", u"\u0415\u0436\u0435\u043c\u0435\u0441\u0435\u0447\u043d\u0430\u044f \u043f\u0440\u0438\u0431\u044b\u043b\u044c:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u043e\u0438\u0442 \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043d\u0430 \u0434\u0440\u0443\u0433\u0438\u0435 \u043c\u0435\u0441\u0442\u0430.<br />\u0422.\u043a. \u0432 \u0446\u0435\u043b\u043e\u043c \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0435\u043b\u0438 \u043d\u0438\u0436\u0435 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e."
                        "</p></body></html>", None))
    # retranslateUi

