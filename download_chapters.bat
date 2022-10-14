if exist .env (
  py app.py
) else (
  echo. > .env
)
