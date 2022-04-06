import psycopg2

#connect to db
con = psycopg2.connect(
            host = "localhost",
            database = "myDB",
            user = "postgres",
            password = "admin")

#cursor
cur = con.cursor()

#execute query
cur.execute("select id, name, age from people")

rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]} age {r[2]}")

#close cursor
cur.close()

#close connection
con.close()
