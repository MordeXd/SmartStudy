from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from config import Config
from utils import hash_password, check_password
from models import User

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hash_password(request.form['password'])
        role = request.form['role']
        user = User(username=username, email=email, password=password, role=role)
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully!", "success")
        return redirect(url_for('login'))
    return render_template('auth/register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for(f"{user.role}_dashboard"))
        else:
            flash("Login Failed!", "danger")
    return render_template('auth/login.html')

# Dashboards
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    return render_template('admin/dashboard.html')

@app.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    return render_template('teacher/dashboard.html')

@app.route('/student/dashboard')
@login_required
def student_dashboard():
    return render_template('student/dashboard.html')

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
