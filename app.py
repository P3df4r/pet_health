from flask import Flask
from config import Config
from routes.pet_routes import pet_bp
from services.pet_service import mongo

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)

app.register_blueprint(pet_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)