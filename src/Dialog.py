
from PySide6.QtWidgets import QApplication, QDialog
import sys
from setupHelperUI import Ui_Dialog as Ui_DialogHelper
from setupReportHistoryUI import Ui_Dialog as Ui_DialogHistory
from setupReportUI import  Ui_Dialog as Ui_DialogReport
class DialogHelper(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogHelper()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def __call__(self, text):
        self.ui.textBrowser.setText(text)

class DialogHistory(QDialog):
    def __init__(self, func):
        super().__init__()
        self.ui = Ui_DialogHistory()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.SeeReport.clicked.connect(func)

    def __call__(self, text):
        pass
class DialogReport(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogReport()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def __call__(self, text):
        pass