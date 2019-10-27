import csv

from app.config import Config
from app.database import db
from app.models import Product
from app.schemes import ProductSchema


class SyncDataFromFile(object):
    _batch_size = 20
    _header = ('name', 'photo_url', 'barcode', 'price', 'sku', 'producer')
    _schema_class = ProductSchema

    def fetch(self, path):
        try:
            with open(path) as file:
                chunk = []
                data = csv.DictReader(file, self._header)
                for index, line in enumerate(data):
                    if index % self._batch_size == 0 and index > 0:
                        yield chunk
                        del chunk[:]
                    chunk.append(line)
                yield chunk
        except Exception as e:
            print(str(e))

    def run(self):
        path = Config.DATA_SOURCE_FILE
        if path:
            for batch in self.fetch(path):
                self.process_save({item['sku']: item for item in batch})

    def process_save(self, _data):
        schema = self._schema_class()
        for product in Product.query.filter(
                Product.sku.in_(_data.keys())).all():
            product_data = _data.pop(product.sku)
            errors = schema.validate(product_data)
            if not errors:
                product_data.update({'id': product.id})
                db.session.merge(Product(**product_data))

        if _data:
            data_to_create = [
                item for item in _data.values() if not schema.validate(item)
            ]
            db.session.bulk_insert_mappings(Product, data_to_create)
        db.session.commit()
