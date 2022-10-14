# Scrapping web SX3 del grupo TV3 (Cataluña, España)

### Autor: [Santiago Martínez](https://github.com/santimb96)
### Versión: 1.0.1
### Fecha: 2022-10-14

## Descripción
#### Script para descargar capítulos de las series de la web [SX3](https://www.ccma.cat/tv3/sx3/) del grupo TV3 (Cataluña, España)

## Requisitos

* Python 3.6 o superior

* En el .env se debe especificar la URL de la serie:
    * URL_BASE=https://www.ccma.cat/tv3/sx3/detectiu-conan/
    * API_URL=https://api-media.ccma.cat/pvideo/media.jsp?media=video&versio=vast&idint=

* En el directorio raíz del proyecto, hacemos lo siguiente:
    * `py -m venv nombrequequieras`
    * `.\nombrequequieras\Scripts\activate`
    * `pip install -r requirements.txt`

## Uso

En el directorio raíz del proyecto, tras hacer lo anterior, ejecutamos en el terminal lo siguiente:
* `python main.py`

!!!! IMPORTANTE: Al ejecutarlo puede devolvernos un error 403 (acceso prohibido) a la web. Supongo que la web quizás detecta peticiones fuera de lo común y no nos deja siempre entrar. Solo hay que seguir ejecutando el comando hasta que evalúe los capítulos y los descargue o no.