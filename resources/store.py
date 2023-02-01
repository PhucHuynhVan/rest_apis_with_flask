# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema, StoreUpdateSchema

store_blp = Blueprint("Stores", __name__, description="Operations on store")


@store_blp.route("/store")
class StoreList(MethodView):
    """Method for Stores"""

    def get(self):
        return {"stores": list(stores.values())}

    @store_blp.arguments(StoreSchema)
    def post(self, store_date):
        for store in stores.values():
            if store_date["name"] == store["name"]:
                abort(400, message="Store already exists.")
        store_id = uuid.uuid4().hex
        store = {**store_date, "id": store_id}
        stores[store_id] = store
        return store, 201


@store_blp.route("/store/<string:store_id>")
class Store(MethodView):
    """Method for individual store"""

    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    @store_blp.arguments(StoreUpdateSchema)
    def put(self, store_data, store_id):
        try:
            store = stores[store_id]
            store |= store_data
            return store
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
