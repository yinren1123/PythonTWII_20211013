import 資料擷取.BWIBBU as bwi
import sqlite3
import time
def drop_table():
    sql = '''
        drop table BWIBBU;
    '''

#symbol + ts 複合索引鍵
def create_table():
    sql = '''
            create table if not exists BWIBBU(
                id integer primary key not null,
                symbol varchar(20) not null,
                name varchar(20) not null,
                yieid float not null,
                pe float not null,
                pb float not null,
                ts date 
              ) 
        '''
    conn = sqlite3.connect('tw_stock.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def create_record(list):
    sql = "insert into BWIBBU(symbol, name, yieid, pe, pb , ts) values (?, ?, ?, ?, ?, ?)"
    conn = sqlite3.connect('tw_stock.db')
    cursor = conn.cursor()
    cursor.executemany(sql, list)
    conn.commit()
    conn.close()
    print('insert ok')

if __name__ == '__main__':
    # homework 將 10/11 月份的資料匯入到資料庫

    list = bwi.getData(2021, 11, 3)
    print(len(list), list)
    create_table()
    create_record(list)
    time.sleep(10)  # 每一次爬蟲之後要停10秒

