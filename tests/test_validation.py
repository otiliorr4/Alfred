import pytest

from alfred.tools.validation import validar_argumentos


def test_permite_youtube():
    resultado = validar_argumentos(
        "abrir_pagina_web",
        '{"nombre": "youtube"}'
    )

    assert resultado == {"nombre": "youtube"}


def test_rechaza_programa_no_autorizado():
    with pytest.raises(ValueError):
        validar_argumentos(
            "abrir_programa",
            '{"nombre": "powershell"}'
        )