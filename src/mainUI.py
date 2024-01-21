from src.GUI.setupUI import Ui_BuisnessCalc as Ui_MainWindow
from src.GUI.Dialog import *
from src.oracle import Oracle_SQL
import pickle
import threading

AVG_CHECK_COMMON = {'Москва': 900, 'Санкт-Питербург': 850}
AVG_CHECK_FAST = {'Москва': 700, 'Санкт-Питербург': 650}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.ui.i_TC1.setFocus()
        def __buttons_connect():
            # Главные кнопки
            self.ui.rep_history.clicked.connect(lambda: self.__history_dialog())
            self.ui.rep_create.clicked.connect(lambda: self.__report_create())
            self.ui.admin.clicked.connect(lambda: self.__user_panel())
            self.ui.profile.clicked.connect(lambda: self.__profile_dialog())

            # Хелперы
            self.ui.h_TC1.clicked.connect(lambda: self.__helper_dialog('Стоимость помещения, которое будет куплено под заведение (руб)'))
            self.ui.h_TC2.clicked.connect(lambda: self.__helper_dialog('Стоимость ремонта помещения, который необходим для того, чтобы оно стало соответствовать всем заданным параметрам (функционал, интерьер, экстерьер и т.д.) (руб)'))
            self.ui.h_TC3.clicked.connect(lambda: self.__helper_dialog('Стоимость всего необходимого оборудования и инвентаря, которое планируется к приобретению или в длительный лизинг (руб)'))
            self.ui.h_TC4.clicked.connect(lambda: self.__helper_dialog('Планируемые траты на пиар-кампанию заведения (руб)'))
            self.ui.h_TC5.clicked.connect(lambda: self.__helper_dialog('Сумма денег, которую федеральные или региональные власти, могут выделить для развития бизнеса единожды (руб)'))
            self.ui.h_TC6.clicked.connect(lambda: self.__helper_dialog('Среднемесячная стоимость ингредиентов, необходимых для приготовления блюд из меню (руб)'))
            self.ui.h_TC7.clicked.connect(lambda: self.__helper_dialog('Ежемесячная сумма, выплачиваемая по процентам банку, на закрытие суммы долга'))
            self.ui.h_TC8.clicked.connect(lambda: self.__helper_dialog('Сумма ежемесячной заработной платы сотрудников заведения'))
            self.ui.h_TC9.clicked.connect(lambda: self.__helper_dialog('Сумма, которую планируется потратить на оплату годового страхования бизнеса и уплату налогов (руб)'))
            self.ui.h_TC10.clicked.connect(lambda: self.__helper_dialog('Среднемесячная стоимость уборки и технического обслуживания помещений (руб)'))
            self.ui.h_TC11.clicked.connect(lambda: self.__helper_dialog('Среднемесячная сумма оплаты за коммунальный услуг (руб)'))
            self.ui.h_TC12.clicked.connect(lambda: self.__helper_dialog('Среднемесячная сумма затрат на логистику (доставки, подвоз продуктов и и т.д) (руб)'))
            self.ui.h_TC13.clicked.connect(lambda: self.__helper_dialog('Сумма, которую планируется потратить на продолжение пиар-кампании заведения (руб)'))

            self.ui.h_TR1_2.clicked.connect(lambda: self.__helper_dialog('Количество заведений похожего типа (фаст-фуд, столовая и т.д.) в радиусе 300 м от выбранного места заведения'))
            self.ui.h_TR2_1.clicked.connect(lambda: self.__helper_dialog('Средний доход с каждого заказа посетителя (руб)'))
            self.ui.h_TR2_2.clicked.connect(lambda: self.__helper_dialog('Средний доход с каждого заказа посетителя в заведения похожего типа в городе городе (руб)'))
            self.ui.h_TR2_3.clicked.connect(lambda: self.__helper_dialog('Среднемесячная заработная плата жителей данного города за месяц'))
            self.ui.h_TR3_1.clicked.connect(lambda: self.__helper_dialog('Количество людей, проживающих рядом с заведением в радиусе 500 м\nСайт партнёр для рассчёта: https://gisbuyer.com/'))
            self.ui.h_TR3_2.clicked.connect(lambda: self.__helper_dialog('Количество людей, проходящих через данную область, радиуса 300 м, за определённый промежуток времени (проходимость места)'))
            self.ui.h_TR3_3.clicked.connect(lambda: self.__helper_dialog('Суммарное количество остановок общественного транспорта и станций метро рядом с заведением в радиусе 300 м'))
        __buttons_connect()
    @classmethod
    def __helper_dialog(cls, text):
        cls.helper.show()
        cls.helper(text)
    @classmethod
    def __history_dialog(cls):
        if cls.get_access_lvl()[3]:
            cls.history.show()
            cls.history.raise_()
            cls.th_history = threading.Thread(target=lambda: cls.history(Oracle_SQL.get_history_data()))
            cls.th_history.start()
    @classmethod
    def report_dialog(cls):
        selected = cls.history.get_selected_CASE_ID()
        if selected:
            cls.report.show()
            cls.report.raise_()
            cls.report(Oracle_SQL.get_report_data(selected))

    @classmethod
    def __user_panel(cls):
        if cls.get_access_lvl()[5]:
            cls.user_panel.show()
            cls.user_panel.raise_()
            cls.user_panel(Oracle_SQL.get_user_data())
    @classmethod
    def user_panel_refresh(cls):
        cls.user_panel(Oracle_SQL.get_user_data())
    @classmethod
    def user_edit(cls):
        selected = cls.user_panel.get_selected_login()
        if selected:
            cls.user_editUI.show()
            cls.user_editUI.raise_()
            cls.user_editUI(Oracle_SQL.get_user_data(USER = selected, PASSWORD = '', PASS_MODE = False))
    @classmethod
    def delete_user(cls):
        selected = cls.user_panel.get_selected_login()
        if selected:
            Oracle_SQL.remove_user(USER = selected)
            cls.user_panel_refresh()
    @classmethod
    def __profile_dialog(cls):
        cls.profile.show()
        cls.profile.raise_()
        cls.profile(*cls.get_access_lvl())
    def __report_create(self):
        if self.get_access_lvl()[4]:
            if self.ui.i_TR2_1.text() != '':
                AVG_CHECK = float(self.ui.i_TR2_1.text())
            elif self.ui.i_TR2_2.currentText() != '...':
                val = self.ui.i_TR2_2.currentText()
                AVG_CHECK = AVG_CHECK_COMMON[val] if self.ui.i_TR1_1.currentText() == 'Обычный' else AVG_CHECK_FAST[val]
            elif self.ui.i_TR2_3.text() != '':
                #AVG_CHECK = float(self.ui.i_TR2_3.text())
                AVG_CHECK = 0
            else:
                AVG_CHECK = 0
            Oracle_SQL.add_report(float(self.ui.i_TC1.text()),
                                  float(self.ui.i_TC2.text()),
                                  float(self.ui.i_TC3.text()),
                                  float(self.ui.i_TC4.text()),
                                  float(self.ui.i_TC5.text()),
                                  float(self.ui.i_TC6.text()),
                                  float(self.ui.i_TC7.text()),
                                  float(self.ui.i_TC8.text()),
                                  float(self.ui.i_TC9.text()),
                                  float(self.ui.i_TC10.text()),
                                  float(self.ui.i_TC11.text()),
                                  float(self.ui.i_TC12.text()),
                                  float(self.ui.i_TC13.text()),
                                  self.ui.i_TR1_1.currentText(),
                                  float(self.ui.i_TR1_2.text()),
                                  AVG_CHECK,
                                  float(self.ui.i_TR3_1.text()),
                                  float(self.ui.i_TR3_2.text()),
                                  float(self.ui.i_TR3_3.text()),
                                  self.ui.i_TR4_1.text(),
                                  self.ui.i_TR4_2.text()
                                  )
    @classmethod
    def get_access_lvl(cls):
        try:
            with open('user_data.pkl', 'rb') as file:
                user_data = pickle.load(file)
                access = Oracle_SQL.get_user_data(*user_data)
                if access:
                    access = access[0]
                    if access[5]:
                        access[4], access[3] = 1, 1
                    return access
                else:
                    return '', '', 'не авторизован', 0, 0, 0
        except:
            return '', '', 'не авторизован', 0, 0, 0
    @classmethod
    def profile_log(cls):
        with open('user_data.pkl', 'wb') as file:
            user_data = [*cls.profile.get_log_data()]
            pickle.dump(user_data, file)
        cls.profile(*cls.get_access_lvl())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow.helper = DialogHelper()
    MainWindow.report = DialogReport()
    MainWindow.history = DialogHistory(lambda: MainWindow.report_dialog())
    MainWindow.user_editUI = DialogUserEdit(MainWindow.user_panel_refresh)
    MainWindow.user_panel = DialogUsers(*[lambda: MainWindow.user_edit()], MainWindow.user_panel_refresh, MainWindow.delete_user)
    MainWindow.profile = DialogProfile(lambda: Oracle_SQL.add_user(MainWindow.profile.ui.r_fio.text(), MainWindow.profile.ui.r_email.text(), MainWindow.profile.ui.r_log.text().lower(), MainWindow.profile.ui.r_pass.text()),
                                       lambda: MainWindow.profile_log())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())