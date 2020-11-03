import psycopg2

con = psycopg2.connect(
    host = 'user',
    database = 'contacts',
    user = 'postgres',
    password = '5937111',
    port = '5432',
)

cur = con.cursor()

cur.execute('insert into contacts (names, numbers) values (%s, $s)', ('Komron', '998935937111'))

cur.execute('select names, numbers from contacts')

rows = cur.fetchall()

for r in rows:
    print('names {r[0]} numbers {r[1]}')

con.commit()

cur.cursor()

con.close()