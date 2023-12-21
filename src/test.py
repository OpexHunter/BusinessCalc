
from PySide6.QtWidgets import QApplication, QDialog
import sys
from setupHelperUI import Ui_Dialog
class DialogWindow(QDialog):
    def __init__(self):
        super(DialogWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def __call__(self, text):
        self.ui.textBrowser.setText(text)