import setup

controls=setup.setup()
cur=controls[1]
sql=controls[0]

def insertvisitor(data):
    cur.execute(f"insert into visitor values {data}")
    sql.commit()

def insertstudent(data):
    cur.execute(f"insert into student values {data}")
    sql.commit()

def deletestudent(data):
    try:
        cur.execute(f"delete from student where student_id={data}")
        sql.commit()
    except:pass

def insertcanteen(data):
    cur.execute(f"insert into canteen values {data}")
    sql.commit()
    
def viewstudent():
    cur.execute("select * from student")
    return cur.fetchall()

def viewvisitor():
    cur.execute("select * from visitor")
    return cur.fetchall()

def viewcanteen():
    cur.execute("select * from canteen")
    data=cur.fetchall()
    try:
        for i in range(len(data)):
            data[i]=data[i]+(data[i][-1]*3,)
    except:pass
    return data

def messfeeview():
    cur.execute("select * from student")
    return cur.fetchall()

def viewroom(year):
    cur.execute(f"select * from student where yr={year}")
    return cur.fetchall()