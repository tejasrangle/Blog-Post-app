import pymysql as p

def insert_author_data(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="insert into author (username,password,email_id,city) values(%s,%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()

def insert_user_data(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="insert into user (username,password,email_id,city) values(%s,%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()

def check_author(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="select * from author where username=%s and password=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    return data

def insert_blog_data(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="insert into blogs (author_name,blog_title,blog) values(%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()

def show_posts():
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="select * from blogs"
    cur.execute(q)
    data=cur.fetchall()
    return data

def check_user(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="select * from user where username=%s and password=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    return data

def show_post(t):
    con=p.connect(user="root",host="localhost",database="blog_post")
    cur=con.cursor()
    q="select * from blogs where author_name=%s"
    cur.execute(q,t)
    data=cur.fetchall()
    return data




    
