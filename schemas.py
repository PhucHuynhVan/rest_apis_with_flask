# pylint: disable=missing-module-docstring
from marshmallow import Schema, fields


class ItemSchema(Schema):
    """Schemas for individual Item"""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    """Schemas for update individual Item"""

    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    """Schemas for individual Store"""

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class StoreUpdateSchema(Schema):
    """Schemas for update individual Store"""

    name = fields.Str()
