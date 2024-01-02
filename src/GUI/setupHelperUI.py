# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupHelperUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QTextBrowser, QWidget)
from . import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(601, 186)
        icon = QIcon()
        icon.addFile(u":/src_ico/question.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame_help = QFrame(Dialog)
        self.frame_help.setObjectName(u"frame_help")
        self.frame_help.setGeometry(QRect(10, 10, 581, 161))
        self.frame_help.setStyleSheet(u"QFrame#frame_help {\n"
"	background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.frame_help.setFrameShape(QFrame.StyledPanel)
        self.frame_help.setFrameShadow(QFrame.Raised)
        self.textBrowser = QTextBrowser(self.frame_help)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 20, 541, 111))
        self.textBrowser.setStyleSheet(u"QFrame {\n"
"	margin-top: 2px;\n"
"	background-color: rgba(0, 0, 0, 0.00);\n"
"   border: 0px solid rgba(0, 0, 0, 0); border-radius: 0px;\n"
"}")
        self.label = QLabel(self.frame_help)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 451, 31))
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a \u0432\u0432\u043e\u0434\u0430", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">C\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0431\u0443\u0434\u0435\u0442 \u043a\u0443\u043f\u043b\u0435\u043d\u043e \u043f\u043e\u0434 \u0437\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0435 (\u0440\u0443\u0431)</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 | \u041c\u0435\u0442\u043e\u0434\u0438\u043a\u0430 \u0440\u0430\u0441\u0441\u0447\u0451\u0442\u0430:", None))
    # retranslateUi

