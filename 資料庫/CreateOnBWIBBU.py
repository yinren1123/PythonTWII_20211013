import 資料擷取.BWIBBU as bwi
import datetime as dt
import sqlite3
import time


# symbol + ts 複合索引鍵
def create_table():
    sql = '''
            create table if not exists BWIBBU(
                id integer primary key not null,
                symbol varchar(20) not null,
                name varchar(20) not null,
                yield float not null,
                pe float not null,
                pb float not null,
                ts date ,
                CONSTRAINT pk_id_ts unique (id, ts)
              ) ;
        '''
    conn = sqlite3.connect('tw_stock.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def create_record(list):
    sql = "insert into BWIBBU(symbol, name, yield, pe, pb , ts) values (?, ?, ?, ?, ?, ?)"
    conn = sqlite3.connect('tw_stock.db')
    cursor = conn.cursor()
    cursor.executemany(sql, list)
    conn.commit()
    conn.close()
    print("Insert OK")


if __name__ == '__main__':
    create_table()
    # homework 將 10/11 月份的資料匯入到資料庫
    start_date = dt.datetime(2021, 11, 9)
    end_date = dt.datetime(2021, 11, 10)
    total_dates = (end_date - start_date).days + 1
    # 在for迴圈內作業。
    for day in range(total_dates):
        select_date = (start_date + dt.timedelta(days=day)).date()
        now_date = dt.date.today()
        if now_date >= select_date:
            print("資料尚未產生，結束資料抓取")
            break
        else:
            date = select_date.strftime("%Y%m%d")
            print("資料抓取 date :", date)
            create_record(bwi.getData(date))
            time.sleep(5)
