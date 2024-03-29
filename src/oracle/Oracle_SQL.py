import bcrypt
import cx_Oracle
import datetime
cx_Oracle.init_oracle_client(lib_dir="oracle")

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

def add_report(RENT_COST, REPAIR_COST, EQUIP_COST, ADVERTISING_FC, SUBSIDIZING, INGR_COST, CREDIT,
               SALARY, INSURANCE, MAINTENANCE, KU, LOGISTICS, ADVERTISING_VC, RES_TYPE, COMPETITORS,
               AVG_CHECK, RES_TRAFFIC, NODE_TRAFFIC, SIGHT_TRAFFIC, ADDRESS, NAME):

    #Расчёты
    FC = RENT_COST + REPAIR_COST + EQUIP_COST + ADVERTISING_FC - SUBSIDIZING

    if RES_TYPE == 'Обычный':
        RES_DOL, RES_V = 0.0064, 1.2
        NODE_DOL, NODE_V = 0.0054, 1.56
        SIGHT_DOL, SIGHT_V = 0.0068, 1.96
    else:
        RES_DOL, RES_V = 0.00642, 1.08
        NODE_DOL, NODE_V = 0.0013, 1.88
        SIGHT_DOL, SIGHT_V = 0.0079, 1.76

    Q = RES_TRAFFIC * RES_DOL * RES_V * + NODE_TRAFFIC * NODE_DOL * NODE_V / 15 + SIGHT_TRAFFIC * SIGHT_DOL * SIGHT_V
    Q = Q / COMPETITORS

    TR = AVG_CHECK * Q
    VC= INGR_COST + CREDIT+SALARY + INSURANCE + MAINTENANCE + KU + LOGISTICS + ADVERTISING_VC
    PROFIT = TR - VC
    if PROFIT > 0:
        PROFIT *= 0.867
    TIMEE=FC/PROFIT


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

def add_user(FIO , EMAIL, LOGIN, PASSWORD, CAN_SEE = 0, CAN_REPORT = 0, ADMIN = 0):
    data=[(FIO, EMAIL, LOGIN.lower(), str(PASSWORD), CAN_SEE, CAN_REPORT, ADMIN)]
    str_dat=data[0]
    b=len(str_dat) #Авто-заполнение sql запроса
    d='('
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
             INTO USERS VALUES"""+d # d='(:1, :2, ..., :29)'

    cursor.executemany(sql,data)
    connection.commit()

def get_full_report_data(CASE_ID = '0'):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()

    sql = f"""SELECT *
             FROM history
             WHERE CASE_ID = {CASE_ID}
             ORDER BY 1 DESC"""
    result=cursor.execute(sql)

    for row in result:
        return [*list(row)]

def get_report_data(CASE_ID = '0'):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()

    sql = f"""SELECT CASE_ID, ADDRESS, NAME, FC, VC, TR, PROFIT, TIMEE, REPORT_DATE
             FROM history
             WHERE CASE_ID = {CASE_ID}
             ORDER BY 1 DESC"""
    result=cursor.execute(sql)

    for row in result:
        return [*list(row)]

def get_user_data(USER = '', PASSWORD = '', PASS_MODE = True):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()
    bl = True if USER + PASSWORD != "" else False
    USER = "'" + USER + "'"

    sql = (f'SELECT FIO, EMAIL, LOGIN, CAN_SEE, CAN_REPORT, ADMIN, PASSWORD FROM USERS '
           f'{"WHERE LOGIN = " + USER if bl else ""} ORDER BY 1 DESC')
    result=cursor.execute(sql)

    result_return = []
    for row in result:
        result_return.append([*list(row)])
    if len(result_return) == 0:
        return [['', '', 'не авторизован', 0, 0, 0]]

    try:
        if bl and PASS_MODE:
            hash_str = result_return[0][6]
            if hash_str.startswith("b'") and hash_str.endswith("'"):
                hash_bytes = bytes(hash_str[2:-1], 'utf-8').decode('unicode_escape').encode('utf-8')
            else:
                hash_bytes = hash_str.encode('utf-8')
            password_bytes = PASSWORD.encode('utf-8')

            if bcrypt.checkpw(password_bytes, hash_bytes):
                result_return = [sublist[:-1] for sublist in result_return]
                return result_return
            else:
                return None
        else:
            result_return = [sublist[:-1] for sublist in result_return]
            return result_return
    except ValueError:
        print('Invalid salt')
        return [['', '', 'не авторизован', 0, 0, 0]]
def edit_user_data(USER, can_see, can_report, admin):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()
    s = "'"
    sql = (f'UPDATE USERS '
           f'SET CAN_SEE = {can_see}, CAN_REPORT = {can_report}, ADMIN = {admin} '
           f'WHERE LOGIN = {s}{USER}{s}')

    cursor.execute(sql)
    connection.commit()

def remove_user(USER):
    dsn = cx_Oracle.makedsn('91.241.13.247', '1521', service_name='EDU')
    connection = cx_Oracle.connect(user='intern_team5', password='fj493#_8gfhgr',
                                   dsn=dsn)
    cursor = connection.cursor()
    s = "'"
    sql = (f'DELETE FROM USERS '
           f'WHERE LOGIN = {s}{USER}{s}')

    cursor.execute(sql)
    connection.commit()