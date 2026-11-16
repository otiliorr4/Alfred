import logging

from alfred.tools.registry import get_tool
from alfred.tools.validation import validar_argumentos


logger = logging.getLogger(__name__)


def ejecutar_herramienta(nombre, argumentos_json):
    try:
        argumentos = validar_argumentos(nombre, argumentos_json)
    except ValueError as error:
        return {
            "ok": False,
            "error": str(error),
        }

    funcion = get_tool(nombre)

    if funcion is None:
        return {
            "ok": False,
            "error": "Herramienta no registrada.",
        }

    try:
        resultado = funcion(**argumentos)

    except Exception:
        logger.exception("Error ejecutando herramienta: %s", nombre)

        return {
            "ok": False,
            "error": "Error interno al ejecutar la herramienta.",
        }

    return {
        "ok": True,
        "resultado": resultado,
    }