#import flask
from flask import Flask, render_template, request, redirect, url
from flaskext.mysql import MySQL # import flask MySQL

mysql=MySQL()

#initializing Flask components in app variable
app=Flask(__name__)

# configure mysql with flaskk app using app variable
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='pythonsam'
app.config['MYSQL_DATABASE_HOST']='localhost'

# Initialize app
mysql.init_app(app)


#Route for app login page
@app.route("/")
def index():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

#running app
if __name__=="__main__":
    app.run(debug=True)