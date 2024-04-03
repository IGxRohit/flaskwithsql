from flask import Flask,render_template , request,redirect
import mysql.connector

conn = mysql.connector.connect(host = "localhost", username = "root", password = "0121", database = "flaskdatabase")

curser = conn.cursor()

app=Flask(__name__)

@app.route("/aboutus")
def homepage():
    return render_template("aboutus.html")
@app.route("/")
def indexpage():
    return render_template("home.html")
@app.route("/contact")
def contact():
    return render_template("contactus.html")
@app.route("/services")
def services():
    curser.execute("select * from pets")
    alldata=curser.fetchall()
    return render_template("services.html",data=alldata)
@app.route("/findpets")
def findpets():
    return render_template("findpets.html")
    
@app.route("/savedata", methods =["post"])
def savedata():
    if request.method=="POST" :
      title=request.form.get("title")
      msg=request.form.get("msg")
      curser.execute(f"insert into pets values('{title}', '{msg}')")
      conn.commit()
      return redirect("/contact")
    
@app.route("/deletethisdata/<x>", methods = ["POST"])
def deletethisdata(x):
    curser.execute(f"delete from pets where  title='{x}'")
    return redirect("/services")

@app.route("/updatethisdata/<x>", methods = ["POST"])
def updatethisdata(x):
    curser.execute("select * from pets")
    alldata=curser.fetchall()
    return render_template("update.html",alldata=alldata)


@app.route("/upd/<x>", methods = ["POST"])
def upd(x):
    if request.method=="POST" :
          title=request.form.get("updatetitle")
          Message=request.form.get("updatemessage")
          curser.execute(f" UPDATE pets SET title = title, Message= Message where  title='{x}'")
          return render_template("services.html",)



if __name__=="__main__":
    app.run(port=1000,debug=True)
