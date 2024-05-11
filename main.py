#imports
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#define the sql uri
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aaldb.db'

#define database
db = SQLAlchemy(app)

#define the user model,check the columns we need
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(58), nullable=False)
    lastname = db.Column(db.String(58), nullable=False)
    email = db.Column(db.String(58), nullable=False)
    role = db.Column(db.String(58), nullable=False)

#create tables
def create_db():
    with app.app_context():
        db.create_all()

#create the routes
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def adduser():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lasttname']
        email = request.form['email']
        role = request.form['role']

        new_user = User(firstname=firstname, lastname=lastname, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html', title='Add a user')

if __name__ == '__main__':
    create_db()
    app.run(port=8080, debug=True)
