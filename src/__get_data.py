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

#в переменной CASE_ID хранится номер кейса расчёта (НАДО ПОЛУЧИТЬ ЗНАЧЕНИЕ CASE_ID человеческим способом)
CASE_ID=2

# в переменную sql пишем текст запроса
sql = """SELECT *
         FROM history
         where CASE_ID=
         """+str(CASE_ID)

#в переменную result кладем результат запроса
result=cursor.execute(sql)

#переменная result имеет тип переменной "cx_oracle.cursor" тут преобразуем её в list
#чтобы из листа распихать по переменным
# просто list(result) почему-то не сработал, но сработало так
for row in result:
    st=list(row)
#в переменной st находится list, где каждый элемент соответсвует значению из БД по порядку

#тут из нашего list st распихиваем по отдельным переменным
RENT_COST=st[1]
REPAIR_COST=st[2]
EQUIP_COST=st[3]
ADVERTISING_FC=st[4]
SUBSIDIZING=st[5]
INGR_COST=st[6]
CREDIT=st[7]
SALARY=st[8]
INS_TAXES=st[9]
MAINTENANCE=st[10]
KU=st[11]
LOGISTICS=st[12]
ADVERTISING_VC=st[13]
RES_SPECIFIC=st[14]
RES_TYPE=st[15]
COMPETITORS=st[16]
AVG_CHECK=st[17]
CITY=st[18]
AVG_SALARY=st[19]
RES_TRAFFIC=st[20]
NODE_TRAFFIC=st[21]
SIGHT_TRAFFIC=st[22]
ADDRESS=st[23]
VC=st[24]
FC=st[25]
TR=st[26]
PROFIT=st[27]
TIMEE=st[28]

#вывод в виде текста основных результатов (по хорошему это надо в txt или как-нибудь ещё оформить)
print('ОСНОВНЫЕ РЕЗУЛЬТАТЫ РАСЧЁТА:')
print('Время окупаемости бизнеса', TIMEE, 'месяцев');
print('Ожидаемые единоразовые расходы', FC, 'тыс.рублей');
print('Ожидаемые ежимесячные расходы', FC, 'тыс.рублей');
print('Ожидаемый доход ресторана', TR, 'тыс.рублей в месяц');
print('Ожидаемый доход ресторана', TR, 'тыс.рублей в месяц');
print('Ожидаемая ежемесечная прибыль', PROFIT, 'тыс.рублей в месяц');