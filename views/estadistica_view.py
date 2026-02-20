from flask import render_template


class EstadisticaView:

    @staticmethod
    def dashboard(total_clientes, total_ingresos, total_asistencias):
        return render_template(
            "estadisticas/index.html",
            total_clientes=total_clientes,
            total_ingresos=total_ingresos,
            total_asistencias=total_asistencias
        )
