# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from sqlalchemy.exc import SQLAlchemyError
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

item_blp = Blueprint("Items", __name__, description="Operations on item")


@item_blp.route("/item")
class ItemList(MethodView):
    """Method for Items"""

    @item_blp.response(200, ItemSchema(many=True))
    def get(self):
        return "items.values()"

    @item_blp.arguments(ItemSchema)
    @item_blp.response(201)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item")

        return item


# @item_blp.route("/item/<string:item_id>")
# class Item(MethodView):
#     """Method for individual item"""
#
#     @item_blp.response(200, ItemSchema)
#     def get(self, item_id):
#         try:
#             return items[item_id]
#         except KeyError:
#             abort(404, message="Item not found.")
#
#     @item_blp.arguments(ItemUpdateSchema)
#     @item_blp.response(200, ItemSchema)
#     def put(self, item_data, item_id):
#         try:
#             item = items[item_id]
#             item |= item_data
#             return item
#         except KeyError:
#             abort(404, message="Item not found.")
#
#     def delete(self, item_id):
#         try:
#             del items[item_id]
#             return {"message": "Item deleted."}
#         except KeyError:
#             abort(404, message="Item not found.")
