from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates')

@auth_bp.route('/')
def login():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def handle_login():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    # TODO: Add real authentication logic here

    # Redirect based on role
    if role == 'Buyer':
        return redirect(url_for('dashboards_bp.buyer_home'))
    elif role == 'Supplier':
        return redirect(url_for('dashboards_bp.supplier_home'))
    elif role == 'Admin':
        return redirect(url_for('dashboards_bp.admin_home'))
    else:
        return redirect(url_for('auth_bp.login'))  # fallback
    