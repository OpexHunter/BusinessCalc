import cx_Oracle
import datetime

def get_history_data():
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()

    sql = """SELECT CASE_ID, REPORT_DATE, ADDRESS, NAME, RES_TYPE
             FROM history
             ORDER BY 1 DESC
             """
    result=cursor.execute(sql)

    result_return = []
    for row in result:
        result_return.append([*list(row)])
    return result_return

def calc_and_load_report(RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT,
                  SALARY, INSURANCE,MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_TYPE, COMPETITORS,
                  AVG_CHECK,RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, NAME):

    #Расчёты
    FC = RENT_COST + REPAIR_COST + EQUIP_COST + ADVERTISING_FC + SUBSIDIZING
    Q=RES_TRAFFIC+NODE_TRAFFIC+SIGHT_TRAFFIC
    TR=AVG_CHECK*Q
    TAX_RATE=0.1 #налог
    INS_TAXES=TAX_RATE*TR
    VC=INGR_COST+CREDIT+SALARY + INSURANCE +MAINTENANCE+KU+LOGISTICS+ADVERTISING_VC
    VC=VC+INS_TAXES
    TIMEE=FC/(TR-VC)
    PROFIT=TR-VC

    REPORT_DATE = datetime.datetime.now()
    data=[(REPORT_DATE, RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT,
                  SALARY, INSURANCE, MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_TYPE, COMPETITORS,
                  AVG_CHECK,RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, NAME, VC, FC, TR, PROFIT, TIMEE)]
    str_dat=data[0] #для определения длины

    b=len(str_dat) #Авто-заполнение sql запроса
    d='(history_id_seq.nextval, '
    for i in range(b):
        d=d+':'+str(i+1)+','
        if i+1==b:
            d=d[:-1]
            d=d+')'

    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()

    sql = """INSERT
             INTO HISTORY VALUES"""+d # d='(:1, :2, ..., :29)'

    cursor.executemany(sql,data)
    connection.commit()

def get_report_data(CASE_ID):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()

    sql = f"""SELECT CASE_ID, ADDRESS, NAME, FC, VC, TR, PROFIT, TIMEE
             FROM history
             WHERE CASE_ID = {CASE_ID}
             ORDER BY 1 DESC"""
    result=cursor.execute(sql)

    for row in result:
        return [*list(row)]