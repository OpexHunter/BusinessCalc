from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem, QTableView, \
    QVBoxLayout, QWidget
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

    def __call__(self, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['id', 'Дата', 'Адресс', 'Имя', 'Тип ресторана'])
        for id, date, address, name, type in data:
            model.appendRow(
                [QStandardItem(str(id)), QStandardItem(str(date)), QStandardItem(address), QStandardItem(name),
                 QStandardItem(type)])
        self.ui.HistoryTable.setModel(model)
        self.ui.HistoryTable.setColumnWidth(0, 50)
        self.ui.HistoryTable.setColumnWidth(1, 130)
        self.ui.HistoryTable.setColumnWidth(2, 350)
        self.ui.HistoryTable.setColumnWidth(3, 244)
        self.ui.HistoryTable.setColumnWidth(4, 90)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.HistoryTable.setEditTriggers(QTableView.NoEditTriggers)
    def get_selected_CASE_ID(self):
        selected = self.ui.HistoryTable.selectedIndexes()
        if selected:
            for index in selected:
                return self.ui.HistoryTable.model().item(index.row(), 0).text()
class DialogReport(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogReport()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def __call__(self, data):
        self.ui.ReportData.setText(f'CASE_ID = {data[0]} | ADDRESS = {data[1]} | NAME = {data[2]}')
        self.ui.rep1.setText(f'Стартовые расходы (FC): {round(data[3])} р.')
        self.ui.rep2.setText(f'Ежемесячные расходы (VC): {round(data[4])} р.')
        self.ui.rep3.setText(f'Выручка ресторана (TR): {round(data[5])} р.')
        self.ui.rep4.setText(f'Прибыль (PROFIT): {round(data[6])} р.')
        self.ui.rep5.setText(f'Время окупаемости: {int(data[7])} месяцев')
        if data[6] / data[4] > 0.2:
            self.ui.rep_dop.setText(f'Условия старта хорошие, бизнесс можно открывать.\n'
                                    f'Рентабельность: {round(data[6] / data[4], 2) * 100}%')
        elif data[6] / data[4] > 0.1:
            self.ui.rep_dop.setText(f'Стоит посмотреть и на другие возможные места для бизнеса.\n'
                                    f'Рентабельность: {round(data[6] / data[4], 2) * 100}%')
        else:
            self.ui.rep_dop.setText(f'Стоит посмотреть и на другие возможные места для бизнеса.\n'
                                    f'Рентабельность: {round(data[6] / data[4], 2) * 100}%')