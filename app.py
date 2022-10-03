import sqlite3
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///:db.sqlite' # relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/') 

def index():
    #show all todos
    Todo_list = Todo.query.all()
    print(Todo)
    return render_template ('index.html')

#app.debug = True
#app.run(host= '127.0.0.1' , port = 5000)

if __name__ == '__main__':
    db.create_all()
    
    new_Todo = Todo(title='Todo1', complete = False)
    db.session.add(new_Todo)
    db.session.commit()
    app.run(debug= True )
   