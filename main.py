import cur
import psycopg2

# connect to db
conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='postgres',
    password='258433'
)

# create cursor
cu = conn.cursor()

# execute query
cur.execute("SELECT * FROM user_name")

cur.fetchfall()

rows = cur.fetchhall()
for row in rows:
    print(row)

#close cursor and connection
cur.close()
conn.close()
