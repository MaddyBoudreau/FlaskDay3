import imp
from flask import Flask, render_template
from . import bp as app

@app.route("/blog")
def blog_file():
    return render_template('blog.html')