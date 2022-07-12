import imp
from flask import Flask, render_template


#DEFINING THE APP FUNCTION 
def create_app():
    app = Flask(__name__)

    #HOME RENDERING

    @app.route("/")
    def home():
        return render_template('index.html')

    #REGISTER RENDERING

    @app.route("/register")
    def about():
        return render_template('register.html')

    #LOGIN RENDERING

    @app.route("/login")
    def contact():
        return render_template('login.html')
    
    #ABOUT RENDERING

    @app.route("/about")
    def blog():
        return render_template('about.html')
    
    #BLOG RENDERING

    @app.route("/blog")
    def blog_file():
        return render_template('blog.html')

#returning the application
    return app