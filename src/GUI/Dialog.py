from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem, QTableView, \
    QVBoxLayout, QWidget
import sys
from .setupHelperUI import Ui_Dialog as Ui_DialogHelper
from .setupReportHistoryUI import Ui_Dialog as Ui_DialogHistory
from .setupReportUI import  Ui_Dialog as Ui_DialogReport
from .setupUserPanelUI import  Ui_Dialog as Ui_DialogUsers
from .setupUserEditUI import Ui_Dialog as Ui_DialogUserEdit
from .setupProfileUI import Ui_Dialog as Ui_DialogProfile

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
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.HistoryTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
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

class DialogUsers(QDialog):
    def __init__(self, func):
        super().__init__()
        self.ui = Ui_DialogUsers()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.commit.clicked.connect(func)
    def __call__(self, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Ф.И.О.', 'Логин', 'Уровень доступа'])
        for FIO, LOGIN, can_see, can_report, admin in data:
            LVL_ACCESS = (f'{"просмотр" if can_see else ""}{", "if can_see and can_report else ""}{"создание отчётов" if can_report else ""}'
                          f'{", "if (admin and can_report) or (not(can_report) and can_see and admin) else ""}'
                          f'{"админ" if admin else ""}{"доступ отсутствует"if not(admin or can_report or can_see) else ""}')
            model.appendRow([QStandardItem(FIO), QStandardItem(LOGIN), QStandardItem(LVL_ACCESS)])
        self.ui.UserTable.setModel(model)
        self.ui.UserTable.setColumnWidth(0, 328)
        self.ui.UserTable.setColumnWidth(1, 200)
        self.ui.UserTable.setColumnWidth(2, 336)
        self.ui.UserTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.UserTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.UserTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.UserTable.setEditTriggers(QTableView.NoEditTriggers)

class DialogUserEdit(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogUserEdit()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
    def __call__(self, data):
        self.ui.checkBox.setChecked(True)

class DialogProfile(QDialog):
    def __init__(self, reg_func, log_func):
        super().__init__()
        self.ui = Ui_DialogProfile()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.r_button.clicked.connect(reg_func)
        self.ui.l_button.clicked.connect(log_func)
    def __call__(self, login = 'не авторизован', can_see = 0, can_report = 0, admin = 0):
        self.ui.i_name.setText(f'Пользователь: {login}')
        self.ui.i_access.setText(f'Уровень доступа: {"просмотр" if can_see else ""}{", "if can_see and can_report else ""}{"создание отчётов" if can_report else ""}'
                                 f'{", "if (admin and can_report) or (not(can_report) and can_see and admin) else ""}{"админ" if admin else ""}'
                                 f'{"доступ отсутствует"if not(admin or can_report or can_see) else ""}')
    def get_log_data(self):
        return self.ui.l_log.text(), self.ui.l_pass.text()