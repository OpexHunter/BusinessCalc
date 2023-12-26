#СКРИПТ РАБОТАЕТ ЧИСТО НА РАСЧЁТ+ЗАГРУЗКУ В ТАБЛИЦУ HISTORY
#НАДО ДОБАВИТЬ ЧЕЛОВЕЧЕСКИЙ ВВОД/ВЫВОД ПАРАМЕТРОВ
import cx_Oracle #импортирование библиотеки для связи с ораклом

# параметры для расчёта FC ФИКСИРОВАННЫЕ ИЗДЕРЖКИ названия переменных взяты из таблицы HISTORY и полностью совпадают
RENT_COST=1000;
REPAIR_COST=100;
EQUIP_COST=500;
ADVERTISING_FC=120;
SUBSIDIZING=50;

#расчёт FC
FC=RENT_COST+REPAIR_COST+EQUIP_COST+ADVERTISING_FC+SUBSIDIZING;

# параметры для расчёта VC переменные ИЗДЕРЖКИ названия переменных  взяты из таблицы HISTORY и полностью совпадают
INGR_COST=150;
CREDIT=30;
SALARY=200;
MAINTENANCE=40;
KU=30;
LOGISTICS=100;
ADVERTISING_VC=30;
RES_SPECIFIC=10;
RES_TYPE='Кафе';
COMPETITORS=3;
AVG_CHECK=0.4;
CITY='Санкт-Петербург';
AVG_SALARY=50;
RES_TRAFFIC=1000;
NODE_TRAFFIC=1500;
SIGHT_TRAFFIC=300;
ADDRESS='ул.Профессора Попова'

#расчёт итогового трафика
Q=RES_TRAFFIC+NODE_TRAFFIC+SIGHT_TRAFFIC;
#расчёт выручки TR
TR=AVG_CHECK*Q;
#расчёт налога на основе 10% от выручки
TAX_RATE=0.1;
INS_TAXES=TAX_RATE*TR;

#расчёт переменных издержек (немного криво написал) два раза VC
VC=INGR_COST+CREDIT+SALARY+MAINTENANCE+KU+LOGISTICS+ADVERTISING_VC+RES_SPECIFIC;
VC=VC+INS_TAXES;

#расчёт ожидаемого времени окупаемости
TIMEE=FC/(TR-VC);

#расчёт ожидаемой прибыли
PROFIT=TR-VC;
#вручную прописываем номер кейса (следует автоматизировать)
CASE_ID=2;

#вывод в виде текста основных результатов
print('ОСНОВНЫЕ РЕЗУЛЬТАТЫ РАСЧЁТА:')
print('Время окупаемости бизнеса', TIMEE, 'месяцев');
print('Ожидаемые единоразовые расходы', FC, 'тыс.рублей');
print('Ожидаемые ежимесячные расходы', FC, 'тыс.рублей');
print('Ожидаемый доход ресторана', TR, 'тыс.рублей в месяц');
print('Ожидаемый доход ресторана', TR, 'тыс.рублей в месяц');
print('Ожидаемая ежемесечная прибыль', PROFIT, 'тыс.рублей в месяц');

#data это переменная типа list, необходимая для выполнения строчки "cursor.executemany(sql,data)"
data=[(CASE_ID, RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT, SALARY, INS_TAXES, MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_SPECIFIC, RES_TYPE, COMPETITORS, AVG_CHECK, CITY, AVG_SALARY, RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, VC, FC, TR, PROFIT, TIMEE)];
#так как len(data)=1 перепишем её в другом виде в переменную str_dat, где len(data)=29, т. е. количество наших атрибутов
str_dat=[CASE_ID, RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT, SALARY, INS_TAXES, MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_SPECIFIC, RES_TYPE, COMPETITORS, AVG_CHECK, CITY, AVG_SALARY, RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, VC, FC, TR, PROFIT, TIMEE];

#в нашем случае необходимо добавить к запросу строчку где будет написано такое (:1, :2 ... :29)
#в ручную 29 раз писать лень, плюс количество атрибутов может измениться, поэтому немного автоматизировал это дело
b=len(str_dat); #количество атрибутов
d='(' #начало строки открываем кавычки
# переменная d это та строка, которая будет добавляться к запросу
#в этом цикле к переменной d добавляем следующий текст ":номер атрибута,"
for i in range(b):
    d=d+':'+str(i+1)+','
    if i+1==b: # проверка на последний элемент, если последний, то закрываем скобку
        d=d[:-1]
        d=d+')'


#прописываем адрес БД
dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')


# Устанавливаем соединение с БД
connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                               dsn=dsn)


# Объявляем курсор. Курсор – это средство извлечения данных из базы данных Oracle.
cursor = connection.cursor()

# в переменную sql пишем текст запроса
sql = """INSERT
         INTO HISTORY VALUES"""+d # d='(:1, :2, ..., :29)'
#запросом вставляем в таблицу HISTORY результат расчёта

#выполнение текста запроса, ввод строк
cursor.executemany(sql,data)

#подверждение ввода строк. Без этой команды строки в таблицу не добавятся
connection.commit()   #без коммита данные в бд не загрузятся


