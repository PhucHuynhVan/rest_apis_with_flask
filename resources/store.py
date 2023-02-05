# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models import StoreModel
from schemas import StoreSchema, StoreUpdateSchema

store_blp = Blueprint("Stores", __name__, description="Operations on store")


@store_blp.route("/store")
class StoreList(MethodView):
    """Method for Stores"""

    @store_blp.response(200, StoreSchema(many=True))
    def get(self):
        return "stores.values()"

    @store_blp.arguments(StoreSchema)
    @store_blp.response(201, StoreSchema)
    def post(self, store_date):
        store = StoreModel(**store_date)
        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating the store")
        except IntegrityError:
            abort(400, message="A store with that name already exists")
        return store


# @store_blp.route("/store/<string:store_id>")
# class Store(MethodView):
#     """Method for individual store"""
#
#     @store_blp.response(200, StoreSchema)
#     def get(self, store_id):
#         try:
#             return stores[store_id]
#         except KeyError:
#             abort(404, message="Store not found.")
#
#     @store_blp.arguments(StoreUpdateSchema)
#     @store_blp.response(200, StoreSchema)
#     def put(self, store_data, store_id):
#         try:
#             store = stores[store_id]
#             store |= store_data
#             return store
#         except KeyError:
#             abort(404, message="Store not found.")
#
#     def delete(self, store_id):
#         try:
#             del stores[store_id]
#             return {"message": "Store deleted."}
#         except KeyError:
#             abort(404, message="Store not found.")
