import sqlite3
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///:db.sqlite' # relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/') 

def index():
    return render_template ('index.html')

#app.debug = True
#app.run(host= '127.0.0.1' , port = 5000)

if __name__ == '__main__':
    db.create_all ()
    app.run(debug= True )
   