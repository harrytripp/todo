from flask import Flask
from flask import request
from markupsafe import escape

# example using escape to protect against injection attacks when returning html
#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"
#app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
	return "Hello World!"

def todoList():
    if request.method == 'POST':
        return addTask()
    else:
        return showTasks()

def addTask():
		return "Task added!"

def showTasks():
		return "List of tasks"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)