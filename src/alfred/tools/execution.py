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

    except ValueError:
        logger.exception("Solicitud inválida: %s", nombre)

        return {
            "ok": False,
            "codigo": "SOLICITUD_INVALIDA",
            "error": "La solicitud no está permitida.",
        }

    except OSError:
        logger.exception("Error del sistema: %s", nombre)

        return {
            "ok": False,
            "codigo": "ERROR_SISTEMA",
            "error": "El sistema operativo no pudo completar la acción.",
        }

    except RuntimeError:
        logger.exception("Fallo de operación: %s", nombre)

        return {
            "ok": False,
            "codigo": "OPERACION_FALLIDA",
            "error": "No se pudo completar la operación solicitada.",
        }

    except Exception:
        logger.exception("Error inesperado: %s", nombre)

        return {
            "ok": False,
            "codigo": "ERROR_INTERNO",
            "error": "Ocurrió un error interno al ejecutar la herramienta.",
        }

    return {
        "ok": True,
        "resultado": resultado,
    }