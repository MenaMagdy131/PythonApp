from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Employee
from . import db, bcrypt

main = Blueprint('main', __name__)

# Home
@main.route('/')
@login_required
def home():
    return render_template('home.html')

# Register
@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('تم إنشاء الحساب بنجاح!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html')

# Login
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('تم تسجيل الدخول بنجاح!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('البريد الإلكتروني أو كلمة المرور غير صحيحة', 'danger')
            return redirect(url_for('main.login'))
    return render_template('login.html')

# Logout
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('تم تسجيل الخروج', 'info')
    return redirect(url_for('main.login'))

# Profile
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# Change Password
@main.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        old_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        if bcrypt.check_password_hash(current_user.password, old_password):
            current_user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            db.session.commit()
            flash('تم تغيير كلمة المرور', 'success')
            return redirect(url_for('main.profile'))
        else:
            flash('كلمة المرور القديمة غير صحيحة', 'danger')
    return render_template('change_password.html')

# Add Employee
@main.route('/employees/add', methods=['GET', 'POST'])
@login_required
def add_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        position = request.form.get('position')
        email = request.form.get('email')
        emp = Employee(name=name, position=position, email=email)
        db.session.add(emp)
        db.session.commit()
        flash('تم إضافة الموظف', 'success')
        return redirect(url_for('main.show_employees'))
    return render_template('add_employee.html')

# Show Employees
@main.route('/employees')
@login_required
def show_employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)