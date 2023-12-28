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

def get_data():
    # в переменную sql пишем текст запроса
    sql = """SELECT REPORT_DATE, ADDRESS, NAME, RES_TYPE
             FROM history
             """

    #в переменную result кладем результат запроса
    result=cursor.execute(sql)

    #переменная result имеет тип переменной "cx_oracle.cursor" тут преобразуем её в list
    #чтобы из листа распихать по переменным
    # просто list(result) почему-то не сработал, но сработало так
    result_return = []
    for row in result:
        st=list(row)
        #в переменной st находится list, где каждый элемент соответсвует значению из БД по порядку

        #тут из нашего list st распихиваем по отдельным переменным
        REPORT_DATE = st[0]
        ADDRESS = st[1]
        NAME = st[2]
        RES_TYPE = st[3]

        result_return.append([REPORT_DATE, ADDRESS, NAME, RES_TYPE])
    return result_return