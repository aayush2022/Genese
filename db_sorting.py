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

print("Unsorted database is:")
for r in rows:
    print (f"id {r[0]} name {r[1]} age {r[2]}")



def sort(rows):

    for r in range(len(rows)-1, 0, -1):
        for j in range(r):
            if rows[j][2]>rows[j+1][2]:
                temp = rows[j]
                rows[j] = rows[j+1]
                rows[j+1] = temp
    return rows            

result = sort(rows)

print("Database sorted by age:")
for r in result: 
    print (f"id {r[0]} name {r[1]} age {r[2]}")


#close cursor
cur.close()

#close connection
con.close()
