from flask import *
import dbmodule as db

app=Flask(__name__)

@app.route("/")
def main_fun():
    return render_template("mainpage.html")

@app.route("/register_author")
def register_au():
    return render_template("register_author.html")

@app.route("/save_author_link",methods=["POST"])
def save_author_data():
    username=request.form["uname"]
    passward=request.form["pwd"]
    email=request.form["email"]
    city=request.form["city"]
    t=(username,passward,email,city)
    db.insert_author_data(t)
    return render_template("register_author.html")

@app.route("/register_user")
def register_u():
    return render_template("register_user.html")

@app.route("/save_user_link",methods=["POST"])
def save_user_data():
    username=request.form["uname"]
    passward=request.form["pwd"]
    email=request.form["email"]
    city=request.form["city"]
    t=(username,passward,email,city)
    db.insert_user_data(t)
    return render_template("register_user.html")

@app.route("/login_author")
def login_au():
    return render_template("login_author.html")

@app.route("/check_author_link",methods=["POST"])
def check_author():
    global username1
    username1=request.form["uname"]
    passward=request.form["pwd"]
    t=(username1,passward)
    data=db.check_author(t)
    if data:
        return render_template("author_interface.html")
    else:
        return render_template("notok.html")

@app.route("/add_post")
def add_post():
    t=username1
    return render_template("add_post.html",res=t)

@app.route("/save_post_link",methods=["POST"])
def save_post_data():
    author_name=request.form["author_name"]
    blog_title=request.form["blog_title"]
    blog=request.form["blog"]
    t=(author_name,blog_title,blog)
    db.insert_blog_data(t)
    return render_template("add_post.html")

@app.route("/view_post")
def view_post():
    t=(username1)
    data=db.show_post(t)
    if data:
        return render_template("view_post.html",res=data)
    else:
        return render_template("no_post.html")

@app.route("/login_user")
def login_u():
    return render_template("login_user.html")

@app.route("/check_user_link",methods=["POST"])
def check_user():
    username=request.form["uname"]
    passward=request.form["pwd"]
    t=(username,passward)
    data=db.check_user(t)
    if data:
        data=db.show_posts()
        return render_template("view_post.html",res=data)  
    else:
        return render_template("notok.html")

@app.route("/action",methods=["POST"])
def action():
    au_name=request.form["author"]
    t=(au_name)
    data=db.show_post(t)
    return render_template("action_post.html",res=data) 


if __name__=="__main__":
    app.run(debug=True)