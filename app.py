from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user, login_required
from datetime import datetime
import pickle
from pytz import timezone

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Caitlyn123@localhost/fakenews'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

with open('rmodel', 'rb') as file:
    loaded_model = pickle.load(file)

with open('vector.pkl', 'rb') as file:
    loaded_vector = pickle.load(file)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.String(255), nullable=False)
    psw = db.Column(db.String(1000), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone('Asia/Kolkata')))

    def __repr__(self):
        return f'<User {self.email}>'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['umail']
        user = Users.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('index'))
        else:
            if current_user.is_authenticated and current_user.account_type == 'admin':
                User = Users(name=request.form['uname'], email=email,
                             phone=request.form['ucontact'], psw=request.form['upass'],
                             account_type=request.form['utype'])
            else:
                User = Users(name=request.form['uname'], email=email,
                             phone=request.form['ucontact'], psw=request.form['upass'],
                             account_type='user')
            db.session.add(User)
            db.session.commit()
            if current_user.is_authenticated:
                if current_user.account_type == "Owner":
                    return redirect(url_for('index'))
            else:
                return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = Users.query.filter_by(email=email).first()
        if user:
            if user.psw == request.form['password']:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Wrong Password!', 'danger')
                return redirect(url_for('index'))
        else:
            flash('User not found!', 'danger')
            return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You Have Been Logged Out!", 'success')
    return redirect(url_for('index'))


@app.route("/admin_index")
def admin_index():
    return render_template("admin_index.html")


@app.route("/user_index")
def user_index():
    return render_template("user_index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if not current_user.is_authenticated:
        flash('Login to access the page!', 'warning')  # Flash message with 'warning' category
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            data = request.form['message']

           
            pred = loaded_model.predict(loaded_vector.transform([data]))
            if pred == 1:
                flash('The Given news is Fake', 'danger')
            else:
                flash('The Given news is Real', 'success')
        return render_template('prediction.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


