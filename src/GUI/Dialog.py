import PySide6
import pandas as pd
from PySide6.QtCore import QBuffer, QIODevice
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QHeaderView, QTableWidgetItem, QTableView, \
    QVBoxLayout, QWidget, QGraphicsView
import sys

from .setupHelperUI import Ui_Dialog as Ui_DialogHelper
from .setupReportHistoryUI import Ui_Dialog as Ui_DialogHistory
from .setupReportUI import  Ui_Dialog as Ui_DialogReport
from .setupUserPanelUI import  Ui_Dialog as Ui_DialogUsers
from .setupUserEditUI import Ui_Dialog as Ui_DialogUserEdit
from .setupProfileUI import Ui_Dialog as Ui_DialogProfile
from src.oracle import Oracle_SQL

from .barReport import BarGramm
from PIL import Image
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.lib.utils import ImageReader

import subprocess
import os

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
        self.ui.refresh.clicked.connect(lambda: self.__call__(Oracle_SQL.get_history_data()))

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
        self.ui.HistoryTable.setColumnWidth(3, 220)
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
        self.ui.save_pdf.clicked.connect(self.save_pdf)
        self.ui.save_folder_open.clicked.connect(self.open_save_dir)
        self.ui.save_xlsx.clicked.connect(self.save_excel)

    def save_excel(self):
        data = Oracle_SQL.get_full_report_data(self.kesh_id)
        list_index = list(['Покупка помещения',
                           'Ремонт',
                           'Оборудование',
                           'Реклама (стартовая)',
                           'Cубсидирование',
                           'Себестоимость ингридиентов',
                           '% кредита',
                           'ЗП',
                           'Страхование',
                           'Уборка,тех.обслуживание',
                           'Коммунальные услуги',
                           'Логистика',
                           'Реклама (после старта)',
                           'Трафик проживающих(500м)',
                           'Узловой трафик',
                           'Трафик мест скопления',
                           'Тип ресторана',
                           'Кол-во конкурентов',
                           'Средний чек',
                           'ВСЕГО'])

        df = pd.DataFrame({
            'FC' : {
                list_index[0] : data[2],    #Покупка помещения
                list_index[1] : data[3],    #Ремонт
                list_index[2] : data[4],    #Оборудование
                list_index[3] : data[5],    #Реклама (стартовая)
                list_index[4] : data[6],    #Cубсидирование
                list_index[19] :data[24]},  #Всего
            'VC' : {
                list_index[5] : data[7],    #Себестоимость ингридиентов
                list_index[6] : data[8],    #% кредита
                list_index[7] : data[9],    #ЗП
                list_index[8] : data[10],   #Страхование
                list_index[9] : data[11],   #Уборка,тех.обслуживание
                list_index[10] :data[12],   #Коммунальные услуги
                list_index[11] :data[13],   #Логистика
                list_index[12] :data[14],   #Реклама (после старта)
                list_index[19] :data[23]},  #Всего
            'TR' : {
                list_index[13] : data[18],  #Трафик проживающих(500м)
                list_index[14] : data[19],  #Узловой трафик
                list_index[15] : data[20],  #Трафик мест скопления
                list_index[19] : data[25]}, #Всего
            'Данные предприятия' : {
                list_index[16] : data[15],  #Тип ресторана
                list_index[17] : data[16],  #Кол-во конкурентов
                list_index[18] : data[17]}, #Средний чек
            'Прибыль' : {
                list_index[19] : data[26]}, #Всего
            'Окупаемость': {
                 list_index[19] : data[27]} #Всего
        }, index = list_index)
        excel_path = f"reports/report-{self.kesh_data.strftime('%d.%m.%Y')} {self.kesh_name}.xlsx"
        df.to_excel(excel_path)

    def save_pdf(self):
        pixmap = self.grab()

        qimage = pixmap.toImage()
        buffer = QBuffer()
        buffer.open(QIODevice.ReadWrite)
        qimage.save(buffer, "PNG")
        pil_im = Image.open(BytesIO(buffer.data()))

        # Обрезаем изображение
        cropped_img = pil_im.crop((0, 0, 741, 398))

        # Создаем PDF с подходящим размером страницы и ориентацией
        pdf_path = f"reports/report-{self.kesh_data.strftime('%d.%m.%Y')} {self.kesh_name}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=landscape((741, 398)))

        # Получаем байтовый поток из обрезанного изображения
        img_byte_arr = BytesIO()
        cropped_img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Вставляем изображение, выравнивая его по верхнему левому углу страницы
        c.drawImage(ImageReader(img_byte_arr), 0, 0, width=741, height=398, mask='auto')
        c.save()

    def updateCanvas(self, canvas):
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().setParent(None)
        self.ui.verticalLayout_2.addWidget(canvas)

    def open_save_dir(self):
        # Текущий путь
        current_dir = os.path.dirname(os.path.abspath(__name__))
        # Переход в папку reports
        reports_dir_path = os.path.join(current_dir, 'reports')

        if not os.path.exists(reports_dir_path):
            os.makedirs(reports_dir_path)

        if os.name == 'nt':  # Если операционная система Windows
            subprocess.run(['explorer', reports_dir_path])
        elif os.name == 'posix':
            if sys.platform == 'darwin':  # MacOS
                subprocess.run(['open', reports_dir_path])
            else:  # Большинство дистрибутивов Linux, Unix, и т.д.
                subprocess.run(['xdg-open', reports_dir_path])
        else:
            raise RuntimeError("Неподдерживаемая операционная система")

    def __call__(self, data):
        self.kesh_name = data[2]
        self.kesh_data = data[8]
        self.kesh_id = data[0]
        self.ui.ReportData.setText(f'CASE_ID = {data[0]} | ADDRESS = {data[1]} | NAME = {data[2]}')
        self.ui.rep1.setText(f'Стартовые расходы (FC): {round(data[3])} р.')
        self.ui.rep2.setText(f'Ежемесячные расходы (VC): {round(data[4])} р.')
        self.ui.rep3.setText(f'Выручка ресторана (TR): {round(data[5])} р.')
        self.ui.rep4.setText(f'Прибыль (PROFIT): {round(data[6])} р.')
        self.ui.rep5.setText(f'Время окупаемости: {int(data[7])} месяцев')
        if data[6] / data[4] > 0.2:
            self.ui.rep_dop.setText(f'Условия старта хорошие, бизнесс можно открывать.\n'
                                    f'Рентабельность: {round(data[6] / data[4] * 100, 2)}%')
        elif data[6] / data[4] > 0.1:
            self.ui.rep_dop.setText(f'Стоит посмотреть и на другие возможные места для бизнеса.\n'
                                    f'Рентабельность: {round(data[6] / data[4]  * 100, 2)}%')
        else:
            self.ui.rep_dop.setText(f'Стоит посмотреть и на другие возможные места для бизнеса.\n'
                                    f'Рентабельность: {round(data[6] / data[4]  * 100, 2)}%')

        index = list(['FC', 'VC', 'TR', 'PROFIT'])
        values = list([data[3], data[4], data[5], data[6]])
        self.ui.figure = BarGramm()
        self.ui.figure.graph(self, index, values)
class DialogUsers(QDialog):
    def __init__(self, func1, func2, func3):
        super().__init__()
        self.ui = Ui_DialogUsers()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.commit.clicked.connect(func1)
        self.ui.refresh.clicked.connect(func2)
        self.ui.remove.clicked.connect(func3)
    def __call__(self, data):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Ф.И.О.', 'Логин', 'Уровень доступа'])
        for FIO, EMAIL, LOGIN, can_see, can_report, admin in data:
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
    def get_selected_login(self):
        selected = self.ui.UserTable.selectedIndexes()
        if selected:
            for index in selected:
                return self.ui.UserTable.model().item(index.row(), 1).text()

class DialogUserEdit(QDialog):
    def __init__(self, func):
        super().__init__()
        self.ui = Ui_DialogUserEdit()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        def save(login, can_see, can_report, admin):
            Oracle_SQL.edit_user_data(login, can_see, can_report, admin)
            func()
            self.close()
        self.ui.b_save.clicked.connect(lambda: save(self.ui.l_login.text(), 1 if self.ui.can_see.isChecked() else 0, 1 if self.ui.can_report.isChecked() else 0, 1 if self.ui.admin.isChecked() else 0))
    def __call__(self, data):
        #data = FIO, EMAIL, LOGIN, CAN_SEE, CAN_REPORT, ADMIN
        data = data[0]
        self.ui.l_fio_email.setText(f'{data[0]} | e-mail: {data[1]}')
        self.ui.l_login.setText(f'{data[2]}')
        self.ui.can_see.setChecked(data[3])
        self.ui.can_report.setChecked(data[4])
        self.ui.admin.setChecked(data[5])


class DialogProfile(QDialog):
    def __init__(self, reg_func, log_func):
        super().__init__()
        self.ui = Ui_DialogProfile()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.r_button.clicked.connect(reg_func)
        self.ui.l_button.clicked.connect(log_func)
    def __call__(self, fio = '', email = '', login = 'не авторизован', can_see = 0, can_report = 0, admin = 0):
        self.ui.i_name.setText(f'Пользователь: {login}')
        self.ui.i_access.setText(f'Уровень доступа: {"просмотр" if can_see else ""}{", "if can_see and can_report else ""}{"создание отчётов" if can_report else ""}'
                                 f'{", "if (admin and can_report) or (not(can_report) and can_see and admin) else ""}{"админ" if admin else ""}'
                                 f'{"доступ отсутствует"if not(admin or can_report or can_see) else ""}')
    def get_log_data(self):
        return self.ui.l_log.text(), self.ui.l_pass.text()