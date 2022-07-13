import imp
from flask import Flask, render_template
from . import bp as app
    
#REGISTER RENDERING

@app.route("/register")
def about():
    return render_template('register.html')

#LOGIN RENDERING

@app.route("/login")
def contact():
    return render_template('login.html')