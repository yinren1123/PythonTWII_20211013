import sqlite3

conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
sql = "select * from BWIBBU where pe > 0 and pe < 12 and pb < 1 and yield > 10"
cursor.execute(sql)
row = cursor.fetchall()
for row in row:
    print(row)