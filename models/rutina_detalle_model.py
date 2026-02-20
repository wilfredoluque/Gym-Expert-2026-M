from core.database import db

class RutinaDetalle(db.Model):
    __tablename__ = "rutina_detalle"

    id = db.Column(db.Integer, primary_key=True)
    rutina_id = db.Column(db.Integer, db.ForeignKey("rutinas.id"))
    ejercicio_id = db.Column(db.Integer, db.ForeignKey("ejercicios.id"))
    series = db.Column(db.Integer)
    repeticiones = db.Column(db.Integer)
    peso = db.Column(db.Float)

    rutina = db.relationship("Rutina")
    ejercicio = db.relationship("Ejercicio")

    def __init__(self, rutina_id, ejercicio_id, series, repeticiones, peso):
        self.rutina_id = rutina_id
        self.ejercicio_id = ejercicio_id
        self.series = series
        self.repeticiones = repeticiones
        self.peso = peso

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return RutinaDetalle.query.all()

    @staticmethod
    def get_by_id(id):
        return RutinaDetalle.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
