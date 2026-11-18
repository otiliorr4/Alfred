from unittest.mock import patch

from alfred.tools import register_default_tools
from alfred.tools.execution import ejecutar_herramienta


def test_error_al_abrir_programa():
    register_default_tools()

    with patch(
        "alfred.tools.programs.subprocess.Popen",
        side_effect=OSError("Fallo simulado")
    ):
        resultado = ejecutar_herramienta(
            "abrir_programa",
            '{"nombre": "bloc_de_notas"}'
        )

    assert resultado["ok"] is False
    assert resultado["codigo"] == "ERROR_SISTEMA"
    assert resultado["error"] == (
        "El sistema operativo no pudo completar la acción."
    )
def test_error_al_abrir_pagina_web():
    register_default_tools()

    with patch(
        "alfred.tools.web_pages.webbrowser.open",
        return_value=False
    ):
        resultado = ejecutar_herramienta(
            "abrir_pagina_web",
            '{"nombre": "youtube"}'
        )

    assert resultado["ok"] is False
    assert resultado["codigo"] == "OPERACION_FALLIDA"
    assert resultado["error"] == (
        "No se pudo completar la operación solicitada."
    )
def test_abrir_programa_exitosamente():
    register_default_tools()

    with patch(
        "alfred.tools.programs.subprocess.Popen"
    ) as iniciar_programa:

        resultado = ejecutar_herramienta(
            "abrir_programa",
            '{"nombre": "bloc_de_notas"}'
        )

    assert resultado["ok"] is True
    assert resultado["resultado"] == (
        "Se solicitó abrir: bloc_de_notas"
    )

    iniciar_programa.assert_called_once_with(
        ["notepad.exe"]
    )