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
import src_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(511, 498)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.SeeReport = QPushButton(Dialog)
        self.SeeReport.setObjectName(u"SeeReport")
        self.SeeReport.setGeometry(QRect(380, 460, 121, 31))
        self.HistoryTable = QTableView(Dialog)
        self.HistoryTable.setObjectName(u"HistoryTable")
        self.HistoryTable.setGeometry(QRect(0, 0, 511, 451))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043e\u0442\u0447\u0451\u0442\u043e\u0432", None))
        self.SeeReport.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043e\u0442\u0447\u0451\u0442\u0430", None))
    # retranslateUi

