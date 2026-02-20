from core.database import db
from config.security import hash_password, verify_password

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), default="recepcion")

    def __init__(self, nombre, email, password, rol="recepcion"):
        self.nombre = nombre
        self.email = email
        self.password = hash_password(password)
        self.rol = rol

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()

    def update(self, nombre=None, email=None, rol=None, password=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if rol:
            self.rol = rol
        if password:
            self.password = hash_password(password)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return verify_password(self.password, password)
