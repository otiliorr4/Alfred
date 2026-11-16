import webbrowser


PAGINAS_PERMITIDAS = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
}


def abrir_pagina_web(nombre):
    pagina = PAGINAS_PERMITIDAS.get(nombre.strip().lower())

    if pagina is None:
        raise ValueError(f"Página no permitida: {nombre}")

    resultado = webbrowser.open(pagina)

    if not resultado:
        raise RuntimeError(
            f"No se pudo solicitar abrir: {nombre}"
        )

    return f"Se solicitó abrir: {nombre}"