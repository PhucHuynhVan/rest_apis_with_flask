# pylint: disable=missing-module-docstring
from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    """Schemas for individual Item"""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class ItemUpdateSchema(Schema):
    """Schemas for update individual Item"""

    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class PlainStoreSchema(Schema):
    """Schemas for individual Store"""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class StoreUpdateSchema(Schema):
    """Schemas for update individual Store"""

    name = fields.Str()


class ItemSchema(PlainItemSchema):
    """Schemas for individual Item"""

    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    """Schemas for individual Store"""

    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
