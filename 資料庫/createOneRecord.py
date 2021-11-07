import sqlite3
#建立資料庫與資料表
conn = sqlite3.connect("tw_stock.db")
cursor = conn.cursor()
sql =  "insert into portfolio(symbol, cost, amount, ts )" \
        "values ('%s', %f, %d , '%s')" \
        % ('2330', 499, 500, '2021-11-3')

cursor.execute(sql)
print(cursor.lastrowid)
conn.commit()
conn.close()
