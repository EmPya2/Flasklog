from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/")

def show_form():
    return render_template("form_temp.html")
    
@app.route("/welcome", methods=["POST", "GET"])

def well():
    
    if request.method == "POST":
        a = request.form["name"]
        return redirect(url_for("success", name=a))
        
@app.route("/loginsuccess/<name>")
def success(name): 
    return " Welcome %s"%name
    