from core.database import db

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Producto.query.all()

    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)

    def update(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
