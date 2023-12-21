# step 1: import libraries
from flask import Flask, render_template, url_for, request, redirect
# step 9: import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# step 12: import datetime
from datetime import datetime

# step 2: initialize flask app
app = Flask(__name__)
# step 10: set up database
# /// for relative path; //// for absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# step 11: create database model
# run 'python' in terminal; type 'from app import app, db' in python shell
# type 'app.app_context().push()' in python shell
# type 'db.create_all()' in python shell to create database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# step 3: define routes and functions
# step 13: use decorators to link the function to a url
@app.route('/', methods = ['POST', 'GET'])
def index():
    # step 14: add conditional statement to check if request is POST or GET
    if request.method == 'POST':
        # step 15: get data from form; note the name is 'content'
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task.'
        
    else:
        # step 16: get data from database
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

# step 19: create delete route
# note the use of <int:id> to specify the id of the task to delete
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting that task.'

# step 21: create update route
# note the use of <int:id> to specify the id of the task to update
@app.route('/update/<int:id>', methods=['GET', 'POST'])
# step 24: add function to update task
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    # step 25: add conditional statement
    if request.method == 'POST':
        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating that task.'
        
    else:
        return render_template('update.html', task=task_to_update)

# step 4: run app
# to run app, open terminal; make sure the kernel is activated;
# change into the directory; type 'python app.py' in terminal
if __name__ == '__main__':
    app.run(debug=True)