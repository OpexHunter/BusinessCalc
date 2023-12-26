import sys
import webbrowser
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem, QTableView, \
    QVBoxLayout, QWidget
from setupUI import Ui_BuisnessCalc as Ui_MainWindow
from Dialog import DialogWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        def __setupHelper():
            self.ui.h_TC1.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TC2.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC3.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TC4.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC5.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TC6.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC7.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TC8.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC9.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC10.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC11.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TC12.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC13.clicked.connect(lambda: self.HelpText('sdsad'))
            self.ui.h_TC14.clicked.connect(lambda: self.HelpText('sdsad'))

            self.ui.h_TR1_1.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR1_2.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR2_1.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR2_2.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR2_3.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR3_1.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR3_2.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR3_3.clicked.connect(lambda: self.HelpText('dasd'))
            self.ui.h_TR4_1.clicked.connect(lambda: self.HelpText('dasd'))
        __setupHelper()
    @classmethod
    def HelpText(cls, text):
        cls.helper(text)
        cls.helper.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow.helper = DialogWindow()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())