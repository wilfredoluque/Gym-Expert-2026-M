from core.database import db
from datetime import datetime
from models.producto_model import Producto

class InventarioMovimiento(db.Model):
    __tablename__ = "inventario_movimientos"

    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))
    tipo = db.Column(db.String(20))  # entrada / salida
    cantidad = db.Column(db.Integer)
    fecha = db.Column(db.DateTime, default=datetime.now)

    producto = db.relationship("Producto")

    def __init__(self, producto_id, tipo, cantidad):
        self.producto_id = int(producto_id)
        self.tipo = tipo
        self.cantidad = int(cantidad)

    def save(self):
        producto = Producto.query.get(self.producto_id)
        if not producto:
            return

        if self.tipo == "salida":
            producto.stock -= self.cantidad
        else:
            producto.stock += self.cantidad

        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return InventarioMovimiento.query.order_by(InventarioMovimiento.id.desc()).all()
