from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sruthi11@localhost/UsersData'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.String(20))



@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/add', methods=["POST","GET"])
def add():
    if request.method == "POST":
        Name = request.form.get('name')
        Phone = request.form.get('phone')
        new_user = Users(name=Name, phone=Phone)
        db.session.add(new_user)
        db.session.commit()
        return f"Hey, {Name}! Your phone number {Phone} has been added to the database."
    else:
        return "Please submit the form"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
#if __name__ == '__main__':
 #   with app.app_context():
 #       try:
  #          db.create_all()
   #     except Exception as e:
    #        print(f"An error occurred while creating database tables: {e}")
    #app.run(debug=True)