from core.database import db

class Entrenador(db.Model):
    __tablename__ = "entrenadores"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    telefono = db.Column(db.String(50))
    especialidad = db.Column(db.String(120))

    def __init__(self, nombre, telefono, especialidad):
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Entrenador.query.all()

    @staticmethod
    def get_by_id(id):
        return Entrenador.query.get(id)

    def update(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            db.session.commit()

