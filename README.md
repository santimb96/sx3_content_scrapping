# Scrapping web SX3 del grupo TV3 (Cataluña, España)

### Autor: [Santiago Martínez](https://github.com/santimb96)

### Versión: 1.0.1

### Fecha: 2022-10-14

## Descripción

Script para descargar capítulos de las series de la web [SX3](https://www.ccma.cat/tv3/sx3/) del grupo TV3 (Cataluña, España)

Se basa en el listado de capítulos que aparecen en la web. Si posteriormente se añaden nuevos capítulos en un apartado diferente, se editará este programa para readaptarlos.

## Requisitos

- Python 3.6 o superior

- Crear un fichero .env (`echo. > .env` en la consola de comandos) en el directorio raíz del proyecto

- En el .env se debe especificar la URL de la serie:

  - URL_BASE=https://www.ccma.cat/tv3/sx3/detectiu-conan/
  - API_URL=https://api-media.ccma.cat/pvideo/media.jsp?media=video&versio=vast&idint=

- !!!! : En el fichero `urls_example.txt` se encuentran dos series de ejemplo que pueden copiarse una vez creado el .env, donde se especifica `URL_BASE=` pegamos la URL del fichero o bien se puede obtener buscando desde la propia web proporcionada más anteriormente.

- En el directorio raíz del proyecto, hacemos lo siguiente:
  - `py -m venv nombrequequieras`
  - `.\nombrequequieras\Scripts\activate`
  - `pip install -r requirements.txt`
- !!!! : Si dispones de Windows, puedes ejecutar los scripts `activate_venv.bat` y `download_chapters.bat`, los cuales te crean un entornos virtual de desarrollo, este se activa, se instalan los paquetes necesarios y se crea el `.env` en caso de no tenerlo.

## Uso

En el directorio raíz del proyecto, tras hacer lo anterior, ejecutamos en el terminal lo siguiente:

- `python app.py` o bien `download_chapters.bat` si lo tienes todo bien configurado.

!!!! : Al ejecutarlo puede devolvernos un error 403 (acceso prohibido) a la web. Supongo que la web quizás detecta peticiones fuera de lo común y no nos deja siempre entrar. Solo hay que seguir ejecutando el comando hasta que evalúe los capítulos y los descargue o no.
