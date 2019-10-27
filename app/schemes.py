from marshmallow import fields
from marshmallow import Schema


class BaseModelSchema(Schema):
    id = fields.Integer()
    created = fields.DateTime()
    modified = fields.DateTime()


class ProductSchema(BaseModelSchema):
    name = fields.String()
    photo_url = fields.String()
    barcode = fields.String()
    price = fields.Integer()
    sku = fields.String()
    producer = fields.String()
