@echo off

cd ..

if not exist .env (
  echo BASE_URL="https://www.ccma.cat/tv3/sx3/yu-yu-hakusho-defensors-mes-enlla/" > .env
  echo API_URL="https://api-media.ccma.cat/pvideo/media.jsp?media=video&versio=vast&idint=" >> .env
)

py app.py