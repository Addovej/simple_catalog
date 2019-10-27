from app import db


class BaseModel(db.Model):
    """
        Base database model.
        Defined id and timestamp (created, modified and deleted) fields.
    """

    __abstract__ = True

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    created = db.Column(
        db.DateTime,
        index=True,
        default=db.func.now()
    )
    modified = db.Column(
        db.DateTime,
        index=True,
        default=db.func.now(),
        onupdate=db.func.now()
    )
    deleted = db.Column(
        db.DateTime,
        index=True,
        nullable=True
    )

    def __commit_insert__(self):
        return

    def __commit_update__(self):
        return

    def __commit_delete__(self):
        return


class Product(BaseModel):
    __tablename__ = 'products'

    name = db.Column(
        db.String(100)
    )
    photo_url = db.Column(
        db.String(100)
    )
    barcode = db.Column(
        db.String(100)
    )
    price = db.Column(
        db.Integer
    )
    sku = db.Column(
        db.String(100),
        index=True,
        unique=True
    )
    producer = db.Column(
        db.String(100),
        index=True
    )

    def __repr__(self):
        return f'<Product[{self.id}: {self.name}]>'
