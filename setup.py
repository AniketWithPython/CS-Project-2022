import mysql.connector as mc

def setup():
    sql=mc.connect(user='root',passwd="dav123",host="localhost")
    cur=sql.cursor()
    try:
        with open(f"./hms.sql") as hms:
            for i in hms:
                cur.execute(i)
    except: pass
    cur.execute("use hostel_management_system")
    return (sql,cur)

