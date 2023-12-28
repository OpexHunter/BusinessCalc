#СКРИПТ РАБОТАЕТ ЧИСТО НА ВЫГРУЗКУ ДАННЫХ ИЗ ТАБЛИЦЫ HISTORY
#И ФОРМИРОВАНИИ СОВСЕМ КОРОТКОГО ОТЧЕТА В ВИДЕ ТЕКСТА РЕЗУЛЬТАТА СКРИПТА
#НАДО ДОБАВИТЬ ФОРМИРОВАНИЕ ОТЧЕТА В ЧЕЛОВЕЧЕСКОМ ВИДЕ TXT ИЛИ ЕЩЁ ЧЕГО-НИБУДЬ
import cx_Oracle #импортирование библиотеки для связи с ораклом

#прописываем адрес БД
dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')


# Устанавливаем соединение с БД
connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                               dsn=dsn)



# Объявляем курсор. Курсор – это средство извлечения данных из базы данных Oracle.
cursor = connection.cursor()

def get_history_data():
    sql = """SELECT CASE_ID, REPORT_DATE, ADDRESS, NAME, RES_TYPE
             FROM history
             """
    result=cursor.execute(sql)

    result_return = []
    for row in result:
        st=list(row)
        id = st[0]
        REPORT_DATE = st[1]
        ADDRESS = st[2]
        NAME = st[3]
        RES_TYPE = st[4]

        result_return.append([id, REPORT_DATE, ADDRESS, NAME, RES_TYPE])
    print(result_return)
    return result_return