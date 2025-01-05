from flask import Flask, request, g
from markupsafe import escape
import sqlite3

# example using escape to protect against injection attacks when returning html
#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"

app = Flask(__name__)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
       
DATABASE = 'app/database.db'

@app.route('/', methods=['GET', 'POST'])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def todoList():
    if request.method == 'POST':
        return addTask()
    else:
        return showTasks()

def addTask():
		return "Task added!"

def showTasks():
		return "List of tasks"

def createTable():
    get_db()
    db.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER, name TEXT, info TEXT)")