import mysql.connector as mc
import stdiomask

def credentials():
    global pwd
    pwd=stdiomask.getpass(prompt='Enter MySQL Password:')

def setup():
    while True:
        try:
            credentials()
            sql=mc.connect(user='root',passwd=pwd,host="localhost")
            cur=sql.cursor()
            break
        except:
            print("Wrong Password")
    try:
        with open(f"./hms.sql") as hms:
            for i in hms:
                cur.execute(i)
    except: pass
    cur.execute("use hostel_management_system")
    return (sql,cur)

