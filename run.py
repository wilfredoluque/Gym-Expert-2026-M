import os
from flask import Flask, request, session, redirect, url_for
from config.settings import Config
from core.database import db
from datetime import datetime

# BLUEPRINTS
from controllers.auth_controller import bp as auth_bp
from controllers.usuarios_controller import bp as usuario_bp
from controllers.clientes_controller import bp as cliente_bp
from controllers.planes_controller import bp as plan_bp
from controllers.membresias_controller import bp as membresia_bp
from controllers.pagos_controller import bp as pago_bp
from controllers.asistencias_controller import bp as asistencias_bp
from controllers.entrenadores_controller import bp as entrenador_bp
from controllers.rutinas_controller import bp as rutina_bp
from controllers.productos_controller import bp as producto_bp
from controllers.inventario_controller import bp as inventario_bp
from controllers.dashboard_controller import bp as dashboard_bp
from controllers.ejercicios_controller import bp as ejercicios_bp
from controllers.estadistica_controller import bp as estadistica_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 🔥 Configurar DB para Render (PostgreSQL)
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        # Render usa postgres:// pero SQLAlchemy necesita postgresql://
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url

    db.init_app(app)

    # ===== REGISTER BLUEPRINTS =====
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(plan_bp)
    app.register_blueprint(membresia_bp)
    app.register_blueprint(pago_bp)
    app.register_blueprint(asistencias_bp)
    app.register_blueprint(entrenador_bp)
    app.register_blueprint(rutina_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(ejercicios_bp)
    app.register_blueprint(estadistica_bp)

    # ===== HELPERS =====
    @app.context_processor
    def utility():
        def is_active(path):
            return "active" if request.path.startswith(path) else ""
        return dict(is_active=is_active)

    @app.context_processor
    def inject_year():
        return {"current_year": datetime.now().year}

    # ===== HOME =====
    @app.route("/")
    def home():
        return "GymExpert funcionando 🚀"

    # 🔐 Protección global
    @app.before_request
    def proteger():
        rutas_libres = ["auth.login", "auth.logout", "auth.register", "static"]

        if request.endpoint not in rutas_libres:
            if "user_id" not in session:
                return redirect(url_for("auth.login"))

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)