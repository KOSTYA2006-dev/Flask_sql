from flask import Flask, url_for, render_template, redirect, request, flash
import data.db_session
from data import db_session
from data.db_session import User, db
from form.user_form import LoginForm, RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
login_manager = LoginManager()
login_manager.login_view = "users.login"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db.init_app(app)

app.config['SECRET_KEY'] = 'zxc'

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    # new_register = User(name='Rost', fname='frost', log='Rosi', password=1234)
    #
    # db.session.add(new_register)
    #
    # db.session.commit()
    return render_template('Photo.html')


# @app.route('/post', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.submit():
#         print(form.log.data)
#         print(222)
#         try:
#             user = User.query.filter_by(log=form.log.data).first()
#
#             if user and user.check_password(form.password.data):
#
#                 return redirect(url_for('/'))
#                 print(111)
#             else:
#                 flash("Invalid Username or password!", "danger")
#         except Exception as e:
#             print(123)
#
#     return render_template('post.html', title='Authorization', form=form)

@app.route("/post", methods=["GET", "POST"])
def login_rote():
    if request.method == "POST":
        log = request.form.get('Login')
        password = request.form.get('Password')
        print(log, password)

        login = User.query.filter_by(log=log, password=password).first()
        if login is not None:
            return redirect("/")
    return render_template("post.html")


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        try:
            name = request.form['name']
            fname = request.form['family']
            log = request.form['log']
            password = request.form['password']
            print(name, fname, log, password)
            new_register = User(name=name, fname=fname, log=log, password=password)

            db.session.add(new_register)

            db.session.commit()

            return redirect('/post')

        except:
           return 'ERROR'

    else:
          return render_template('reg.html')


if __name__ == '__main__':

    app.run(debug=True, port=5005)
