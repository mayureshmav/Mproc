from flask import Flask
from auth.routes import auth_bp
from dashboards.routes import dashboards_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboards_bp)

if __name__ == '__main__':
    app.run(debug=True)