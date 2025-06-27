import json
import pytest
from server.extension import db
from server.models import Plant

class TestPlant:

    def test_plant_by_id_get_route(self, client, app):
        with app.app_context():
            plant = Plant.query.get(1)
            if not plant:
                plant = Plant(name="Test Oak", image="https://example.com/test.jpg", price=100.0, is_in_stock=True)
                db.session.add(plant)
                db.session.commit()

        response = client.get('/plants/1')
        assert response.status_code == 200

    def test_plant_by_id_get_route_returns_one_plant(self, client, app):
        with app.app_context():
            plant = Plant.query.get(1)
            if not plant:
                plant = Plant(name="Test Oak", image="https://example.com/test.jpg", price=100.0, is_in_stock=True)
                db.session.add(plant)
                db.session.commit()

        response = client.get('/plants/1')
        data = json.loads(response.data.decode())
        assert type(data) is dict
        assert data["id"]
        assert data["name"]

    def test_plant_by_id_patch_route_updates_is_in_stock(self, client, app):
        with app.app_context():
            plant = Plant.query.get(1)
            if not plant:
                plant = Plant(name="Live Oak", image="https://example.com/image.jpg", price=250.0, is_in_stock=True)
                db.session.add(plant)
                db.session.commit()

        response = client.patch('/plants/1', json={"is_in_stock": False})
        data = json.loads(response.data.decode())
        assert data["is_in_stock"] is False
