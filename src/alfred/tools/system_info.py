import psutil


def obtener_estado_pc():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()
    bateria = psutil.sensors_battery()

    return {
        "cpu_porcentaje": cpu,
        "ram_total_gib": round(ram.total / (1024 ** 3), 2),
        "ram_disponible_gib": round(ram.available / (1024 ** 3), 2),
        "ram_uso_porcentaje": ram.percent,
        "bateria_porcentaje": (
            bateria.percent if bateria is not None else None
        ),
    }