from core.database import db

class Ejercicio(db.Model):
    __tablename__ = "ejercicios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    grupo_muscular = db.Column(db.String(120))

    def __init__(self, nombre, grupo_muscular):
        self.nombre = nombre
        self.grupo_muscular = grupo_muscular

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Ejercicio.query.all()

    @staticmethod
    def get_by_id(id):
        return Ejercicio.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
