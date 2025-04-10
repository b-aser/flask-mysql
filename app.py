#import flask
from flask import Flask, render_template, request, redirect, url_for
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
@app.route("/", methods=['GET', 'POST'])
def index():
    # first declare error as nNone
    error=None
    con=mysql.connect()
    cur=con.cursor()
    if request.method=='POST':
        uname=request.form['uname']
        passw=request.form['passw']
        cur.execute("SELECT * FROM `users` WHERE `username`='"+uname+"' AND `passw`='"+passw+"'")
        data=cur.fetchone()
        
        # check no data availabile in database
        if data==None:
            error="Data not available or invalid"
            return render_template('login.html', error=error)
        else:
            # check the user name index value
            if uname==data[5] and passw==data[6]:
                return render_template('home.html', data=data)
            else:
                error="Invalid crediential"
                render_template('login.html', error=error)
        
        # if uname=="admin" and passw=="admin":
        #     return render_template('home.html', data=uname)
        # else:
        #     error='Invalid data'
        #     return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    #connectivity code
    con=mysql.connect()
    cur=con.cursor()
    
    if request.method=='POST':
        name=request.form['name']
        phno=request.form['phno']
        gender=request.form['gender']
        dept=request.form['dept']
        uname=request.form['uname']
        passw=request.form['passw']
        cur.execute("INSERT INTO `users`(`name`, `phno`, `gender`, `dept`, `username`, `passw`) VALUES (%s, %s, %s, %s, %s, %s)", (name, phno, gender, dept, uname, passw))
        con.commit()
        return redirect(url_for('index'))
    else:
        return render_template('register.html')

#running app
if __name__=="__main__":
    app.run(debug=True)