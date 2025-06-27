from flask import Flask, jsonify
from server.extension import db
from server.models import Plant

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route('/plants/<int:id>')
    def get_plant(id):
        plant = Plant.query.get(id)
        if plant:
            return jsonify({
                "id": plant.id,
                "name": plant.name,
                "image": plant.image,
                "price": plant.price,
                "is_in_stock": plant.is_in_stock
            })
        return jsonify({"error": "Plant not found"}), 404

    @app.route('/plants/<int:id>', methods=["PATCH"])
    def update_plant(id):
        from flask import request
        plant = Plant.query.get(id)
        if not plant:
            return jsonify({"error": "Plant not found"}), 404
        data = request.get_json()
        plant.is_in_stock = data.get("is_in_stock", plant.is_in_stock)
        db.session.commit()
        return jsonify({
            "id": plant.id,
            "name": plant.name,
            "image": plant.image,
            "price": plant.price,
            "is_in_stock": plant.is_in_stock
        })

    return app
