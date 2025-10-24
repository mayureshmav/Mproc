from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 🔹 MySQL Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayuku@12345",
    database="mproc_db"
)
cursor = db.cursor()

# 🔹 Login Page
@app.route('/')
def login():
    return render_template('login.html')

# 🔹 Handle Login
@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s AND role=%s", (email, password, role))
    user = cursor.fetchone()

    if user:
        if role == 'Buyer':
            return redirect(url_for('buyer_home'))
        elif role == 'Supplier':
            return redirect(url_for('supplier_home'))
    return redirect(url_for('login'))

# 🔹 Buyer Home
@app.route('/buyer/home')
def buyer_home():
    return render_template('buyer_home.html')

# 🔹 Supplier Home
@app.route('/supplier/home')
def supplier_home():
    return render_template('supplier_home.html')

if __name__ == '__main__':
    app.run(debug=True)