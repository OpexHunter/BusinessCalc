import cx_Oracle
import datetime

def calc_and_load(RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT,
                  SALARY, INSURANCE,MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_TYPE, COMPETITORS,
                  AVG_CHECK,RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, NAME):

    FC = RENT_COST + REPAIR_COST + EQUIP_COST + ADVERTISING_FC + SUBSIDIZING
    Q=RES_TRAFFIC+NODE_TRAFFIC+SIGHT_TRAFFIC
    TR=AVG_CHECK*Q
    TAX_RATE=0.1 #налог
    INS_TAXES=TAX_RATE*TR

    VC=INGR_COST+CREDIT+SALARY + INSURANCE +MAINTENANCE+KU+LOGISTICS+ADVERTISING_VC
    VC=VC+INS_TAXES

    #расчёт ожидаемого времени окупаемости
    TIMEE=FC/(TR-VC);

    #расчёт ожидаемой прибыли
    PROFIT=TR-VC;

    REPORT_DATE = datetime.datetime.now()

    #data это переменная типа list, необходимая для выполнения строчки "cursor.executemany(sql,data)"
    data=[(REPORT_DATE, RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT,
                  SALARY, INSURANCE, MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_TYPE, COMPETITORS,
                  AVG_CHECK,RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, NAME, VC, FC, TR, PROFIT, TIMEE)]
    #так как len(data)=1 перепишем её в другом виде в переменную str_dat, где len(data)=29, т. е. количество наших атрибутов
    str_dat=data[0]

    #в нашем случае необходимо добавить к запросу строчку где будет написано такое (:1, :2 ... :29)
    #в ручную 29 раз писать лень, плюс количество атрибутов может измениться, поэтому немного автоматизировал это дело
    b=len(str_dat); #количество атрибутов
    d='(history_id_seq.nextval, ' #начало строки открываем кавычки
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
    print(d)

    #выполнение текста запроса, ввод строк
    cursor.executemany(sql,data)
    connection.commit()