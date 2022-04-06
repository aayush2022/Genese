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


def search(rows, id):  
    for r in rows:  
        if (r[0] == id):  
            return r
    return -1  

id = 4
l = len(rows)   
  
result = search(rows, id)
r = result
if(result == -1):  
    print("ID not found in Database!")  
else:  
    print("Details found: ") 
    print (f"id {r[0]} name {r[1]} age {r[2]}")


    

#close cursor
cur.close()

#close connection
con.close()