from flask import Flask
from config import Config
from models import db
from routes import api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)

app.register_blueprint(api, url_prefix="/api")

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "FoodieHub API is running!"


if __name__ == "__main__":
    app.run(debug=True)

