# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
#import src_rc

class Ui_BuisnessCalc(object):
    def setupUi(self, BuisnessCalc):
        if not BuisnessCalc.objectName():
            BuisnessCalc.setObjectName(u"BuisnessCalc")
        BuisnessCalc.resize(1046, 596)
        icon = QIcon()
        icon.addFile(u":/src_ico/online-shop-_1_.ico", QSize(), QIcon.Normal, QIcon.Off)
        BuisnessCalc.setWindowIcon(icon)
        BuisnessCalc.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgba(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(BuisnessCalc)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TC = QFrame(self.centralwidget)
        self.TC.setObjectName(u"TC")
        self.TC.setGeometry(QRect(10, 10, 371, 571))
        self.TC.setStyleSheet(u"QFrame#TC {\n"
"	background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.TC.setFrameShape(QFrame.StyledPanel)
        self.TC.setFrameShadow(QFrame.Raised)
        self.label_54 = QLabel(self.TC)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 10, 351, 31))
        self.label_54.setStyleSheet(u"QLabel {\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"	margin-left: 1px;\n"
"}")
        self.label_54.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TC2 = QFrame(self.TC)
        self.TC2.setObjectName(u"TC2")
        self.TC2.setGeometry(QRect(0, 40, 361, 201))
        self.TC2.setStyleSheet(u"QFrame#TC2 {\n"
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
        self.TC2.setFrameShape(QFrame.StyledPanel)
        self.TC2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_7 = QWidget(self.TC2)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 160, 341, 29))
        self.horizontalLayout_48 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.layoutWidget_7)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_48)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_48)

        self.i_TC5 = QLineEdit(self.layoutWidget_7)
        self.i_TC5.setObjectName(u"i_TC5")
        self.i_TC5.setMinimumSize(QSize(70, 0))
        self.i_TC5.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_48.addWidget(self.i_TC5)

        self.h_TC5 = QPushButton(self.layoutWidget_7)
        self.h_TC5.setObjectName(u"h_TC5")
        self.h_TC5.setMinimumSize(QSize(23, 24))
        self.h_TC5.setMaximumSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u":/src_ico/question.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.h_TC5.setIcon(icon1)

        self.horizontalLayout_48.addWidget(self.h_TC5)

        self.layoutWidget_4 = QWidget(self.TC2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 100, 341, 31))
        self.horizontalLayout_45 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.layoutWidget_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.label_45)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_45)

        self.i_TC3 = QLineEdit(self.layoutWidget_4)
        self.i_TC3.setObjectName(u"i_TC3")
        self.i_TC3.setMinimumSize(QSize(70, 0))
        self.i_TC3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_45.addWidget(self.i_TC3)

        self.h_TC3 = QPushButton(self.layoutWidget_4)
        self.h_TC3.setObjectName(u"h_TC3")
        self.h_TC3.setMinimumSize(QSize(23, 24))
        self.h_TC3.setMaximumSize(QSize(24, 24))
        self.h_TC3.setIcon(icon1)

        self.horizontalLayout_45.addWidget(self.h_TC3)

        self.layoutWidget_2 = QWidget(self.TC2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 341, 29))
        self.horizontalLayout_43 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.layoutWidget_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 16777215))
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_43)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_43)

        self.i_TC1 = QLineEdit(self.layoutWidget_2)
        self.i_TC1.setObjectName(u"i_TC1")
        self.i_TC1.setMinimumSize(QSize(70, 0))
        self.i_TC1.setMaximumSize(QSize(70, 16777215))
        self.i_TC1.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}\n"
"")

        self.horizontalLayout_43.addWidget(self.i_TC1)

        self.h_TC1 = QPushButton(self.layoutWidget_2)
        self.h_TC1.setObjectName(u"h_TC1")
        self.h_TC1.setMinimumSize(QSize(23, 24))
        self.h_TC1.setMaximumSize(QSize(24, 24))
        self.h_TC1.setStyleSheet(u"QPushButton {\n"
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
        self.h_TC1.setIcon(icon1)

        self.horizontalLayout_43.addWidget(self.h_TC1)

        self.layoutWidget_5 = QWidget(self.TC2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 130, 341, 29))
        self.horizontalLayout_46 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.layoutWidget_5)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.label_46)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_46)

        self.i_TC4 = QLineEdit(self.layoutWidget_5)
        self.i_TC4.setObjectName(u"i_TC4")
        self.i_TC4.setMinimumSize(QSize(70, 0))
        self.i_TC4.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_46.addWidget(self.i_TC4)

        self.h_TC4 = QPushButton(self.layoutWidget_5)
        self.h_TC4.setObjectName(u"h_TC4")
        self.h_TC4.setMinimumSize(QSize(23, 24))
        self.h_TC4.setMaximumSize(QSize(24, 24))
        self.h_TC4.setIcon(icon1)

        self.horizontalLayout_46.addWidget(self.h_TC4)

        self.layoutWidget_3 = QWidget(self.TC2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 70, 341, 29))
        self.horizontalLayout_44 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.layoutWidget_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.label_44)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_44)

        self.i_TC2 = QLineEdit(self.layoutWidget_3)
        self.i_TC2.setObjectName(u"i_TC2")
        self.i_TC2.setMinimumSize(QSize(70, 0))
        self.i_TC2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_44.addWidget(self.i_TC2)

        self.h_TC2 = QPushButton(self.layoutWidget_3)
        self.h_TC2.setObjectName(u"h_TC2")
        self.h_TC2.setMinimumSize(QSize(23, 24))
        self.h_TC2.setMaximumSize(QSize(24, 24))
        self.h_TC2.setIcon(icon1)

        self.horizontalLayout_44.addWidget(self.h_TC2)

        self.label_36 = QLabel(self.TC2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(0, 10, 361, 21))
        self.label_36.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_36.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TC3 = QFrame(self.TC)
        self.TC3.setObjectName(u"TC3")
        self.TC3.setGeometry(QRect(0, 250, 361, 281))
        self.TC3.setStyleSheet(u"QFrame#TC3 {\n"
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
        self.TC3.setFrameShape(QFrame.StyledPanel)
        self.TC3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_12 = QWidget(self.TC3)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(10, 150, 331, 29))
        self.horizontalLayout_53 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.layoutWidget_12)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_53)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_53)

        self.i_TC10 = QLineEdit(self.layoutWidget_12)
        self.i_TC10.setObjectName(u"i_TC10")
        self.i_TC10.setMinimumSize(QSize(70, 0))
        self.i_TC10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_53.addWidget(self.i_TC10)

        self.h_TC10 = QPushButton(self.layoutWidget_12)
        self.h_TC10.setObjectName(u"h_TC10")
        self.h_TC10.setMinimumSize(QSize(23, 24))
        self.h_TC10.setMaximumSize(QSize(24, 24))
        self.h_TC10.setIcon(icon1)

        self.horizontalLayout_53.addWidget(self.h_TC10)

        self.layoutWidget_13 = QWidget(self.TC3)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(10, 90, 331, 31))
        self.horizontalLayout_117 = QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.label_122 = QLabel(self.layoutWidget_13)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_117.addWidget(self.label_122)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_117)

        self.i_TC8 = QLineEdit(self.layoutWidget_13)
        self.i_TC8.setObjectName(u"i_TC8")
        self.i_TC8.setMinimumSize(QSize(70, 0))
        self.i_TC8.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_117.addWidget(self.i_TC8)

        self.h_TC8 = QPushButton(self.layoutWidget_13)
        self.h_TC8.setObjectName(u"h_TC8")
        self.h_TC8.setMinimumSize(QSize(23, 24))
        self.h_TC8.setMaximumSize(QSize(24, 24))
        self.h_TC8.setIcon(icon1)

        self.horizontalLayout_117.addWidget(self.h_TC8)

        self.layoutWidget_100 = QWidget(self.TC3)
        self.layoutWidget_100.setObjectName(u"layoutWidget_100")
        self.layoutWidget_100.setGeometry(QRect(10, 30, 332, 29))
        self.horizontalLayout_142 = QHBoxLayout(self.layoutWidget_100)
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalLayout_142.setContentsMargins(0, 0, 0, 0)
        self.label_149 = QLabel(self.layoutWidget_100)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_142.addWidget(self.label_149)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_142)

        self.i_TC6 = QLineEdit(self.layoutWidget_100)
        self.i_TC6.setObjectName(u"i_TC6")
        self.i_TC6.setMinimumSize(QSize(70, 0))
        self.i_TC6.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_142.addWidget(self.i_TC6)

        self.h_TC6 = QPushButton(self.layoutWidget_100)
        self.h_TC6.setObjectName(u"h_TC6")
        self.h_TC6.setMinimumSize(QSize(23, 24))
        self.h_TC6.setMaximumSize(QSize(24, 24))
        self.h_TC6.setIcon(icon1)

        self.horizontalLayout_142.addWidget(self.h_TC6)

        self.layoutWidget_101 = QWidget(self.TC3)
        self.layoutWidget_101.setObjectName(u"layoutWidget_101")
        self.layoutWidget_101.setGeometry(QRect(10, 120, 331, 29))
        self.horizontalLayout_143 = QHBoxLayout(self.layoutWidget_101)
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.label_150 = QLabel(self.layoutWidget_101)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_143.addWidget(self.label_150)

        self.horizontalSpacer_143 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_143)

        self.i_TC9 = QLineEdit(self.layoutWidget_101)
        self.i_TC9.setObjectName(u"i_TC9")
        self.i_TC9.setMinimumSize(QSize(70, 0))
        self.i_TC9.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_143.addWidget(self.i_TC9)

        self.h_TC9 = QPushButton(self.layoutWidget_101)
        self.h_TC9.setObjectName(u"h_TC9")
        self.h_TC9.setMinimumSize(QSize(23, 24))
        self.h_TC9.setMaximumSize(QSize(24, 24))
        self.h_TC9.setIcon(icon1)

        self.horizontalLayout_143.addWidget(self.h_TC9)

        self.layoutWidget_102 = QWidget(self.TC3)
        self.layoutWidget_102.setObjectName(u"layoutWidget_102")
        self.layoutWidget_102.setGeometry(QRect(10, 60, 331, 29))
        self.horizontalLayout_144 = QHBoxLayout(self.layoutWidget_102)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(0, 0, 0, 0)
        self.label_151 = QLabel(self.layoutWidget_102)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_144.addWidget(self.label_151)

        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_144)

        self.i_TC7 = QLineEdit(self.layoutWidget_102)
        self.i_TC7.setObjectName(u"i_TC7")
        self.i_TC7.setMinimumSize(QSize(70, 0))
        self.i_TC7.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_144.addWidget(self.i_TC7)

        self.h_TC7 = QPushButton(self.layoutWidget_102)
        self.h_TC7.setObjectName(u"h_TC7")
        self.h_TC7.setMinimumSize(QSize(23, 24))
        self.h_TC7.setMaximumSize(QSize(24, 24))
        self.h_TC7.setIcon(icon1)

        self.horizontalLayout_144.addWidget(self.h_TC7)

        self.label_38 = QLabel(self.TC3)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(0, 10, 361, 21))
        self.label_38.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"	margin-left: 3px;\n"
"    font-weight: bold;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_103 = QWidget(self.TC3)
        self.layoutWidget_103.setObjectName(u"layoutWidget_103")
        self.layoutWidget_103.setGeometry(QRect(10, 180, 331, 29))
        self.horizontalLayout_145 = QHBoxLayout(self.layoutWidget_103)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalLayout_145.setContentsMargins(0, 0, 0, 0)
        self.label_152 = QLabel(self.layoutWidget_103)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_145.addWidget(self.label_152)

        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_145)

        self.i_TC11 = QLineEdit(self.layoutWidget_103)
        self.i_TC11.setObjectName(u"i_TC11")
        self.i_TC11.setMinimumSize(QSize(70, 0))
        self.i_TC11.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_145.addWidget(self.i_TC11)

        self.h_TC11 = QPushButton(self.layoutWidget_103)
        self.h_TC11.setObjectName(u"h_TC11")
        self.h_TC11.setMinimumSize(QSize(23, 24))
        self.h_TC11.setMaximumSize(QSize(24, 24))
        self.h_TC11.setIcon(icon1)

        self.horizontalLayout_145.addWidget(self.h_TC11)

        self.layoutWidget_104 = QWidget(self.TC3)
        self.layoutWidget_104.setObjectName(u"layoutWidget_104")
        self.layoutWidget_104.setGeometry(QRect(10, 210, 331, 29))
        self.horizontalLayout_146 = QHBoxLayout(self.layoutWidget_104)
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalLayout_146.setContentsMargins(0, 0, 0, 0)
        self.label_153 = QLabel(self.layoutWidget_104)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_146.addWidget(self.label_153)

        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_146)

        self.i_TC12 = QLineEdit(self.layoutWidget_104)
        self.i_TC12.setObjectName(u"i_TC12")
        self.i_TC12.setMinimumSize(QSize(70, 0))
        self.i_TC12.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_146.addWidget(self.i_TC12)

        self.h_TC12 = QPushButton(self.layoutWidget_104)
        self.h_TC12.setObjectName(u"h_TC12")
        self.h_TC12.setMinimumSize(QSize(23, 24))
        self.h_TC12.setMaximumSize(QSize(24, 24))
        self.h_TC12.setIcon(icon1)

        self.horizontalLayout_146.addWidget(self.h_TC12)

        self.layoutWidget_105 = QWidget(self.TC3)
        self.layoutWidget_105.setObjectName(u"layoutWidget_105")
        self.layoutWidget_105.setGeometry(QRect(10, 240, 331, 29))
        self.horizontalLayout_147 = QHBoxLayout(self.layoutWidget_105)
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.label_154 = QLabel(self.layoutWidget_105)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_147.addWidget(self.label_154)

        self.horizontalSpacer_147 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_147)

        self.i_TC13 = QLineEdit(self.layoutWidget_105)
        self.i_TC13.setObjectName(u"i_TC13")
        self.i_TC13.setMinimumSize(QSize(70, 0))
        self.i_TC13.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_147.addWidget(self.i_TC13)

        self.h_TC13 = QPushButton(self.layoutWidget_105)
        self.h_TC13.setObjectName(u"h_TC13")
        self.h_TC13.setMinimumSize(QSize(23, 24))
        self.h_TC13.setMaximumSize(QSize(24, 24))
        self.h_TC13.setIcon(icon1)

        self.horizontalLayout_147.addWidget(self.h_TC13)

        self.TR = QFrame(self.centralwidget)
        self.TR.setObjectName(u"TR")
        self.TR.setGeometry(QRect(400, 10, 631, 411))
        self.TR.setStyleSheet(u"QFrame#TR {\n"
"   background-color: rgba(0, 0, 0, 0.03);\n"
"   border: 1px solid rgba(0, 0, 0, 0.2); border-radius: 10px;\n"
"}")
        self.TR.setFrameShape(QFrame.StyledPanel)
        self.TR.setFrameShadow(QFrame.Raised)
        self.label_120 = QLabel(self.TR)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(10, 10, 541, 31))
        self.label_120.setStyleSheet(u"QLabel {\n"
"    font-size: 21px;\n"
"    font-weight: bold;\n"
"	margin-left: 10px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_120.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TR2 = QFrame(self.TR)
        self.TR2.setObjectName(u"TR2")
        self.TR2.setGeometry(QRect(0, 40, 501, 61))
        self.TR2.setStyleSheet(u"QFrame#TR2 {\n"
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
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}")
        self.TR2.setFrameShape(QFrame.StyledPanel)
        self.TR2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_80 = QWidget(self.TR2)
        self.layoutWidget_80.setObjectName(u"layoutWidget_80")
        self.layoutWidget_80.setGeometry(QRect(10, 30, 174, 26))
        self.horizontalLayout_115 = QHBoxLayout(self.layoutWidget_80)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_119 = QLabel(self.layoutWidget_80)
        self.label_119.setObjectName(u"label_119")

        self.horizontalLayout_115.addWidget(self.label_119)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_115.addItem(self.horizontalSpacer_115)

        self.i_TR1_1 = QComboBox(self.layoutWidget_80)
        self.i_TR1_1.addItem("")
        self.i_TR1_1.addItem("")
        self.i_TR1_1.addItem("")
        self.i_TR1_1.setObjectName(u"i_TR1_1")
        self.i_TR1_1.setMinimumSize(QSize(80, 0))
        self.i_TR1_1.setStyleSheet(u"")

        self.horizontalLayout_115.addWidget(self.i_TR1_1)

        self.label_39 = QLabel(self.TR2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(0, 10, 501, 21))
        self.label_39.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_79 = QWidget(self.TR2)
        self.layoutWidget_79.setObjectName(u"layoutWidget_79")
        self.layoutWidget_79.setGeometry(QRect(240, 30, 252, 26))
        self.horizontalLayout_114 = QHBoxLayout(self.layoutWidget_79)
        self.horizontalLayout_114.setSpacing(3)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.layoutWidget_79)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_114.addWidget(self.label_118)

        self.horizontalSpacer_114 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_114)

        self.i_TR1_2 = QLineEdit(self.layoutWidget_79)
        self.i_TR1_2.setObjectName(u"i_TR1_2")
        self.i_TR1_2.setMinimumSize(QSize(80, 0))
        self.i_TR1_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_114.addWidget(self.i_TR1_2)

        self.h_TR1_2 = QPushButton(self.layoutWidget_79)
        self.h_TR1_2.setObjectName(u"h_TR1_2")
        self.h_TR1_2.setMinimumSize(QSize(23, 24))
        self.h_TR1_2.setMaximumSize(QSize(24, 24))
        self.h_TR1_2.setIcon(icon1)

        self.horizontalLayout_114.addWidget(self.h_TR1_2)

        self.TR5 = QFrame(self.TR)
        self.TR5.setObjectName(u"TR5")
        self.TR5.setGeometry(QRect(0, 290, 501, 101))
        self.TR5.setStyleSheet(u"QFrame#TR5 {\n"
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
        self.TR5.setFrameShape(QFrame.StyledPanel)
        self.TR5.setFrameShadow(QFrame.Raised)
        self.layoutWidget_75 = QWidget(self.TR5)
        self.layoutWidget_75.setObjectName(u"layoutWidget_75")
        self.layoutWidget_75.setGeometry(QRect(10, 30, 481, 26))
        self.horizontalLayout_110 = QHBoxLayout(self.layoutWidget_75)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_114 = QLabel(self.layoutWidget_75)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_110.addWidget(self.label_114)

        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_110)

        self.i_TR4_1 = QLineEdit(self.layoutWidget_75)
        self.i_TR4_1.setObjectName(u"i_TR4_1")
        self.i_TR4_1.setMinimumSize(QSize(410, 0))
        self.i_TR4_1.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_110.addWidget(self.i_TR4_1)

        self.label_40 = QLabel(self.TR5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(0, 10, 501, 21))
        self.label_40.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_78 = QWidget(self.TR5)
        self.layoutWidget_78.setObjectName(u"layoutWidget_78")
        self.layoutWidget_78.setGeometry(QRect(10, 60, 481, 26))
        self.horizontalLayout_113 = QHBoxLayout(self.layoutWidget_78)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.label_121 = QLabel(self.layoutWidget_78)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_113.addWidget(self.label_121)

        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_113)

        self.i_TR4_2 = QLineEdit(self.layoutWidget_78)
        self.i_TR4_2.setObjectName(u"i_TR4_2")
        self.i_TR4_2.setMinimumSize(QSize(410, 0))
        self.i_TR4_2.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_113.addWidget(self.i_TR4_2)

        self.TR3 = QFrame(self.TR)
        self.TR3.setObjectName(u"TR3")
        self.TR3.setGeometry(QRect(0, 110, 211, 61))
        self.TR3.setStyleSheet(u"QFrame#TR3 {\n"
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
        self.TR3.setFrameShape(QFrame.StyledPanel)
        self.TR3.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.TR3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 10, 181, 21))
        self.label_41.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_73 = QWidget(self.TR3)
        self.layoutWidget_73.setObjectName(u"layoutWidget_73")
        self.layoutWidget_73.setGeometry(QRect(10, 30, 191, 26))
        self.horizontalLayout_108 = QHBoxLayout(self.layoutWidget_73)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_112 = QLabel(self.layoutWidget_73)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_108.addWidget(self.label_112)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_108)

        self.i_TR2_1 = QLineEdit(self.layoutWidget_73)
        self.i_TR2_1.setObjectName(u"i_TR2_1")
        self.i_TR2_1.setMinimumSize(QSize(70, 0))
        self.i_TR2_1.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_108.addWidget(self.i_TR2_1)

        self.h_TR2_1 = QPushButton(self.layoutWidget_73)
        self.h_TR2_1.setObjectName(u"h_TR2_1")
        self.h_TR2_1.setMinimumSize(QSize(23, 24))
        self.h_TR2_1.setMaximumSize(QSize(24, 24))
        self.h_TR2_1.setIcon(icon1)

        self.horizontalLayout_108.addWidget(self.h_TR2_1)

        self.TR3_2 = QFrame(self.TR)
        self.TR3_2.setObjectName(u"TR3_2")
        self.TR3_2.setGeometry(QRect(220, 110, 191, 61))
        self.TR3_2.setStyleSheet(u"QFrame#TR3_2 {\n"
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
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}")
        self.TR3_2.setFrameShape(QFrame.StyledPanel)
        self.TR3_2.setFrameShadow(QFrame.Raised)
        self.label_42 = QLabel(self.TR3_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 10, 181, 21))
        self.label_42.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_107 = QWidget(self.TR3_2)
        self.layoutWidget_107.setObjectName(u"layoutWidget_107")
        self.layoutWidget_107.setGeometry(QRect(10, 30, 161, 26))
        self.horizontalLayout_149 = QHBoxLayout(self.layoutWidget_107)
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_149.setContentsMargins(0, 0, 0, 0)
        self.label_156 = QLabel(self.layoutWidget_107)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_149.addWidget(self.label_156)

        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_149)

        self.i_TR2_2 = QComboBox(self.layoutWidget_107)
        self.i_TR2_2.addItem("")
        self.i_TR2_2.addItem("")
        self.i_TR2_2.setObjectName(u"i_TR2_2")
        self.i_TR2_2.setMinimumSize(QSize(80, 0))
        self.i_TR2_2.setStyleSheet(u"")

        self.horizontalLayout_149.addWidget(self.i_TR2_2)

        self.h_TR2_2 = QPushButton(self.layoutWidget_107)
        self.h_TR2_2.setObjectName(u"h_TR2_2")
        self.h_TR2_2.setMinimumSize(QSize(23, 24))
        self.h_TR2_2.setMaximumSize(QSize(24, 24))
        self.h_TR2_2.setIcon(icon1)

        self.horizontalLayout_149.addWidget(self.h_TR2_2)

        self.TR3_3 = QFrame(self.TR)
        self.TR3_3.setObjectName(u"TR3_3")
        self.TR3_3.setGeometry(QRect(420, 110, 201, 61))
        self.TR3_3.setStyleSheet(u"QFrame#TR3_3 {\n"
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
"}\n"
"\n"
"QComboBox {\n"
"	border: 1px solid rgba(0,0,0,0.2);\n"
"	border-radius: 3px;\n"
"	padding-left: 5px;\n"
"    color: rgb(110, 110, 110);\n"
"}")
        self.TR3_3.setFrameShape(QFrame.StyledPanel)
        self.TR3_3.setFrameShadow(QFrame.Raised)
        self.label_113 = QLabel(self.TR3_3)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(0, 10, 181, 21))
        self.label_113.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_113.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_108 = QWidget(self.TR3_3)
        self.layoutWidget_108.setObjectName(u"layoutWidget_108")
        self.layoutWidget_108.setGeometry(QRect(10, 30, 181, 26))
        self.horizontalLayout_150 = QHBoxLayout(self.layoutWidget_108)
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.horizontalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.label_157 = QLabel(self.layoutWidget_108)
        self.label_157.setObjectName(u"label_157")

        self.horizontalLayout_150.addWidget(self.label_157)

        self.horizontalSpacer_150 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_150.addItem(self.horizontalSpacer_150)

        self.i_TR2_3 = QLineEdit(self.layoutWidget_108)
        self.i_TR2_3.setObjectName(u"i_TR2_3")
        self.i_TR2_3.setMinimumSize(QSize(70, 0))
        self.i_TR2_3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_150.addWidget(self.i_TR2_3)

        self.h_TR2_3 = QPushButton(self.layoutWidget_108)
        self.h_TR2_3.setObjectName(u"h_TR2_3")
        self.h_TR2_3.setMinimumSize(QSize(23, 24))
        self.h_TR2_3.setMaximumSize(QSize(24, 24))
        self.h_TR2_3.setIcon(icon1)

        self.horizontalLayout_150.addWidget(self.h_TR2_3)

        self.TR4 = QFrame(self.TR)
        self.TR4.setObjectName(u"TR4")
        self.TR4.setGeometry(QRect(0, 180, 621, 101))
        self.TR4.setStyleSheet(u"QFrame#TR4 {\n"
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
        self.TR4.setFrameShape(QFrame.StyledPanel)
        self.TR4.setFrameShadow(QFrame.Raised)
        self.label_116 = QLabel(self.TR4)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(0, 10, 501, 21))
        self.label_116.setStyleSheet(u"QLabel {\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"	margin-left: 3px;\n"
"    font-family: \"Noto Sans\";\n"
"}")
        self.label_116.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.layoutWidget_76 = QWidget(self.TR4)
        self.layoutWidget_76.setObjectName(u"layoutWidget_76")
        self.layoutWidget_76.setGeometry(QRect(10, 30, 271, 26))
        self.horizontalLayout_111 = QHBoxLayout(self.layoutWidget_76)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_117 = QLabel(self.layoutWidget_76)
        self.label_117.setObjectName(u"label_117")

        self.horizontalLayout_111.addWidget(self.label_117)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_111)

        self.i_TR3_1 = QLineEdit(self.layoutWidget_76)
        self.i_TR3_1.setObjectName(u"i_TR3_1")
        self.i_TR3_1.setMinimumSize(QSize(70, 0))
        self.i_TR3_1.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_111.addWidget(self.i_TR3_1)

        self.h_TR3_1 = QPushButton(self.layoutWidget_76)
        self.h_TR3_1.setObjectName(u"h_TR3_1")
        self.h_TR3_1.setMinimumSize(QSize(23, 24))
        self.h_TR3_1.setMaximumSize(QSize(24, 24))
        self.h_TR3_1.setIcon(icon1)

        self.horizontalLayout_111.addWidget(self.h_TR3_1)

        self.layoutWidget_74 = QWidget(self.TR4)
        self.layoutWidget_74.setObjectName(u"layoutWidget_74")
        self.layoutWidget_74.setGeometry(QRect(10, 60, 271, 28))
        self.horizontalLayout_109 = QHBoxLayout(self.layoutWidget_74)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.label_115 = QLabel(self.layoutWidget_74)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_109.addWidget(self.label_115)

        self.horizontalSpacer_109 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_109)

        self.i_TR3_3 = QLineEdit(self.layoutWidget_74)
        self.i_TR3_3.setObjectName(u"i_TR3_3")
        self.i_TR3_3.setMinimumSize(QSize(70, 0))
        self.i_TR3_3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_109.addWidget(self.i_TR3_3)

        self.h_TR3_3 = QPushButton(self.layoutWidget_74)
        self.h_TR3_3.setObjectName(u"h_TR3_3")
        self.h_TR3_3.setMinimumSize(QSize(23, 24))
        self.h_TR3_3.setMaximumSize(QSize(24, 24))
        self.h_TR3_3.setIcon(icon1)

        self.horizontalLayout_109.addWidget(self.h_TR3_3)

        self.layoutWidget_77 = QWidget(self.TR4)
        self.layoutWidget_77.setObjectName(u"layoutWidget_77")
        self.layoutWidget_77.setGeometry(QRect(300, 30, 312, 26))
        self.horizontalLayout_112 = QHBoxLayout(self.layoutWidget_77)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.label_158 = QLabel(self.layoutWidget_77)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_112.addWidget(self.label_158)

        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_112)

        self.i_TR3_2 = QLineEdit(self.layoutWidget_77)
        self.i_TR3_2.setObjectName(u"i_TR3_2")
        self.i_TR3_2.setMinimumSize(QSize(70, 0))
        self.i_TR3_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_112.addWidget(self.i_TR3_2)

        self.h_TR3_2 = QPushButton(self.layoutWidget_77)
        self.h_TR3_2.setObjectName(u"h_TR3_2")
        self.h_TR3_2.setMinimumSize(QSize(23, 24))
        self.h_TR3_2.setMaximumSize(QSize(24, 24))
        self.h_TR3_2.setIcon(icon1)

        self.horizontalLayout_112.addWidget(self.h_TR3_2)

        self.rep_create = QPushButton(self.centralwidget)
        self.rep_create.setObjectName(u"rep_create")
        self.rep_create.setGeometry(QRect(400, 430, 191, 61))
        self.rep_history = QPushButton(self.centralwidget)
        self.rep_history.setObjectName(u"rep_history")
        self.rep_history.setGeometry(QRect(600, 430, 181, 61))
        self.rep_progress = QProgressBar(self.centralwidget)
        self.rep_progress.setObjectName(u"rep_progress")
        self.rep_progress.setGeometry(QRect(790, 460, 161, 21))
        self.rep_progress.setValue(0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(790, 440, 71, 16))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(400, 560, 641, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.login = QPushButton(self.layoutWidget)
        self.login.setObjectName(u"login")

        self.horizontalLayout.addWidget(self.login)

        self.admin = QPushButton(self.layoutWidget)
        self.admin.setObjectName(u"admin")

        self.horizontalLayout.addWidget(self.admin)

        BuisnessCalc.setCentralWidget(self.centralwidget)

        self.retranslateUi(BuisnessCalc)

        QMetaObject.connectSlotsByName(BuisnessCalc)
    # setupUi

    def retranslateUi(self, BuisnessCalc):
        BuisnessCalc.setWindowTitle(QCoreApplication.translate("BuisnessCalc", u"\u0411\u0438\u0437\u043d\u0435\u0441\u0441 \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 | \u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u0440\u0435\u043d\u0442\u0430\u0431\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.label_54.setText(QCoreApplication.translate("BuisnessCalc", u"\u0412\u0432\u043e\u0434 \u0438\u0437\u0434\u0435\u0440\u0436\u0435\u043a", None))
        self.label_48.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0443\u0431\u0441\u0438\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 (\u0435\u0434\u0438\u043d\u043e\u0440\u0430\u0437\u043e\u0432\u043e\u0435)", None))
        self.i_TC5.setText("")
        self.i_TC5.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC5.setText("")
        self.label_45.setText(QCoreApplication.translate("BuisnessCalc", u"\u041f\u043e\u043a\u0443\u043f\u043a\u0430 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f/\u043b\u0438\u0437\u0438\u043d\u0433", None))
        self.i_TC3.setText("")
        self.i_TC3.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC3.setText("")
        self.label_43.setText(QCoreApplication.translate("BuisnessCalc", u"\u041f\u043e\u043a\u0443\u043f\u043a\u0430 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f (\u0415\u0441\u043b\u0438 \u043d\u0435 \u0430\u0440\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f)", None))
        self.i_TC1.setText("")
        self.i_TC1.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC1.setText("")
        self.label_46.setText(QCoreApplication.translate("BuisnessCalc", u"\u0420\u0435\u043a\u043b\u0430\u043c\u0430 \u0438 \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433 (\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0435)", None))
        self.i_TC4.setText("")
        self.i_TC4.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC4.setText("")
        self.label_44.setText(QCoreApplication.translate("BuisnessCalc", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u043f\u043e\u0434 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u0435 (\u043f\u0435\u0440\u0435\u0441\u0442\u0440\u043e\u0439\u043a\u0430)", None))
        self.i_TC2.setText("")
        self.i_TC2.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC2.setText("")
        self.label_36.setText(QCoreApplication.translate("BuisnessCalc", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0438\u0437\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_53.setText(QCoreApplication.translate("BuisnessCalc", u"\u0423\u0431\u043e\u0440\u043a\u0430, \u0442\u0435\u0445. \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.i_TC10.setText("")
        self.i_TC10.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC10.setText("")
        self.label_122.setText(QCoreApplication.translate("BuisnessCalc", u"\u0417\u041f, \u0437\u0430\u0442\u0440\u0430\u0442\u044b \u043d\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430", None))
        self.i_TC8.setText("")
        self.i_TC8.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC8.setText("")
        self.label_149.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0438\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442\u043e\u0432 (\u0432 \u043c\u0435\u0441\u044f\u0446)", None))
        self.i_TC6.setText("")
        self.i_TC6.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC6.setText("")
        self.label_150.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0442\u0440\u0430\u0445\u043e\u0432\u0430\u043d\u0438\u0435, \u041d\u0430\u043b\u043e\u0433\u0438", None))
        self.i_TC9.setText("")
        self.i_TC9.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC9.setText("")
        self.label_151.setText(QCoreApplication.translate("BuisnessCalc", u"\u041a\u0440\u0435\u0434\u0438\u0442 (%)", None))
        self.i_TC7.setText("")
        self.i_TC7.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC7.setText("")
        self.label_38.setText(QCoreApplication.translate("BuisnessCalc", u"\u041f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0435 \u0438\u0437\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.label_152.setText(QCoreApplication.translate("BuisnessCalc", u"\u041a\u043e\u043c\u043c\u0443\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.i_TC11.setText("")
        self.i_TC11.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC11.setText("")
        self.label_153.setText(QCoreApplication.translate("BuisnessCalc", u"\u0417\u0430\u0442\u0440\u0430\u0442\u044b \u043d\u0430 \u043b\u043e\u0433\u0438\u0441\u0442\u0438\u043a\u0443", None))
        self.i_TC12.setText("")
        self.i_TC12.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC12.setText("")
        self.label_154.setText(QCoreApplication.translate("BuisnessCalc", u"\u0420\u0435\u043a\u043b\u0430\u043c\u0430 \u0438 \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433 (\u041f\u043e\u0441\u043b\u0435 \u0441\u0442\u0430\u0440\u0442\u0430)", None))
        self.i_TC13.setText("")
        self.i_TC13.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TC13.setText("")
        self.label_120.setText(QCoreApplication.translate("BuisnessCalc", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0440\u0435\u0434\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.label_119.setText(QCoreApplication.translate("BuisnessCalc", u"\u0422\u0438\u043f \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d\u0430", None))
        self.i_TR1_1.setItemText(0, QCoreApplication.translate("BuisnessCalc", u"\u0424\u0430\u0441\u0442 \u0444\u0443\u0434", None))
        self.i_TR1_1.setItemText(1, QCoreApplication.translate("BuisnessCalc", u"\u041e\u0431\u044b\u0447\u043d\u044b\u0439", None))
        self.i_TR1_1.setItemText(2, QCoreApplication.translate("BuisnessCalc", u"\u0414\u043e\u0440\u043e\u0433\u043e\u0439", None))

        self.label_39.setText(QCoreApplication.translate("BuisnessCalc", u"\u0411\u0430\u0437\u043e\u0432\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_118.setText(QCoreApplication.translate("BuisnessCalc", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0442\u043e\u0432", None))
        self.i_TR1_2.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"0", None))
        self.h_TR1_2.setText("")
        self.label_114.setText(QCoreApplication.translate("BuisnessCalc", u"\u0410\u0434\u0440\u0435\u0441 ", None))
        self.i_TR4_1.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0433\u043e\u0440\u043e\u0434, \u0443\u043b\u0438\u0446\u0430, \u0434\u043e\u043c", None))
        self.label_40.setText(QCoreApplication.translate("BuisnessCalc", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_121.setText(QCoreApplication.translate("BuisnessCalc", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.i_TR4_2.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0440\u0435\u0441\u0442\u043e\u0440\u0430\u043d\u0430", None))
        self.label_41.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0447\u0435\u043a (\u043d\u0430\u043f\u0440\u044f\u043c\u0443\u044e)", None))
        self.label_112.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0447\u0435\u043a", None))
        self.i_TR2_1.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TR2_1.setText("")
        self.label_42.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u0447\u0435\u043a (\u041f\u043e \u0433\u043e\u0440\u043e\u0434\u0443)", None))
        self.label_156.setText(QCoreApplication.translate("BuisnessCalc", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.i_TR2_2.setItemText(0, QCoreApplication.translate("BuisnessCalc", u"\u041c\u043e\u0441\u043a\u0432\u0430", None))
        self.i_TR2_2.setItemText(1, QCoreApplication.translate("BuisnessCalc", u"\u0421\u0430\u043d\u043a\u0442-\u041f\u0438\u0442\u0435\u0440\u0431\u0443\u0440\u0433", None))

        self.h_TR2_2.setText("")
        self.label_113.setText(QCoreApplication.translate("BuisnessCalc", u"\u041f\u043e \u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0417\u041f", None))
        self.label_157.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0417\u041f", None))
        self.i_TR2_3.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"\u0440\u0443\u0431.", None))
        self.h_TR2_3.setText("")
        self.label_116.setText(QCoreApplication.translate("BuisnessCalc", u"\u0422\u0440\u0430\u0444\u0438\u043a, \u043f\u043e\u0441\u0435\u0449\u0430\u0435\u043c\u043e\u0441\u0442\u044c Q", None))
        self.label_117.setText(QCoreApplication.translate("BuisnessCalc", u"\u0422\u0440\u0430\u0444\u0438\u043a \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u044e\u0449\u0438\u0445 (500\u043c)", None))
        self.i_TR3_1.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"0", None))
        self.h_TR3_1.setText("")
        self.label_115.setText(QCoreApplication.translate("BuisnessCalc", u"\u0422\u0440\u0430\u0444\u0438\u043a \u043c\u0435\u0441\u0442 \u0441\u043a\u043e\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.i_TR3_3.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"0", None))
        self.h_TR3_3.setText("")
        self.label_158.setText(QCoreApplication.translate("BuisnessCalc", u"\u0423\u0437\u043b\u043e\u0432\u043e\u0439 \u0442\u0440\u0430\u0444\u0438\u043a (\u041c\u0435\u0442\u0440\u043e, \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442)", None))
        self.i_TR3_2.setPlaceholderText(QCoreApplication.translate("BuisnessCalc", u"0", None))
        self.h_TR3_2.setText("")
        self.rep_create.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.rep_history.setText(QCoreApplication.translate("BuisnessCalc", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043e\u0442\u0447\u0451\u0442\u043e\u0432", None))
        self.label.setText(QCoreApplication.translate("BuisnessCalc", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.label_2.setText(QCoreApplication.translate("BuisnessCalc", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0443\u0441\u043f\u0435\u0448\u043d\u0430, \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0434\u043e\u0441\u0442\u0443\u043f\u0430 - \u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))
        self.login.setText(QCoreApplication.translate("BuisnessCalc", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.admin.setText(QCoreApplication.translate("BuisnessCalc", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

