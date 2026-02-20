from core.database import db

class Plan(db.Model):
    __tablename__ = "planes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Float)

    # NUEVO
    tipo_plan = db.Column(db.String(20))  # mensual / sesion

    duracion_dias = db.Column(db.Integer, nullable=True)
    duracion_horas = db.Column(db.Integer, nullable=True)

    descripcion = db.Column(db.String(200))

    def __init__(self, nombre, precio, tipo_plan, duracion_dias=None, duracion_horas=None):
        self.nombre = nombre
        self.precio = precio
        self.tipo_plan = tipo_plan
        self.duracion_dias = duracion_dias
        self.duracion_horas = duracion_horas

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Plan.query.all()

    @staticmethod
    def get_by_id(id):
        return Plan.query.get(id)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()