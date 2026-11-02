import webbrowser


PAGINAS_PERMITIDAS = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
}


def abrir_pagina_web(nombre):
    pagina = PAGINAS_PERMITIDAS.get(nombre.strip().lower())

    if pagina is None:
        return f"Página no permitida: {nombre}"

    try:
        resultado = webbrowser.open(pagina)

        if resultado:
            return f"Se solicitó abrir: {nombre}"

        return f"No se pudo solicitar abrir: {nombre}"

    except (OSError, webbrowser.Error) as error:
        return f"Error al abrir {nombre}: {error}"