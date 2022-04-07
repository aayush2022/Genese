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


def search(rows, student_name):  
    for r in rows:  
        if (r[1] == student_name):  
            return r
    return -1  


student_name = input("Enter the student name you want to find: ")

  
result = search(rows, student_name)

if(result == -1):  
    print("ID not found in Database!")  
else:  
    print("Details found: ") 
    print (f"id {result[0]} name {result[1]} age {result[2]}")


    

#close cursor
cur.close()

#close connection
con.close()
