Set-Location ..

if (-not(Test-Path -Path .\.env -PathType Leaf)){
  # Copy and rename the file:
  Add-Content -Path .env -Value "BASE_URL=https://www.ccma.cat/tv3/sx3/yu-yu-hakusho-defensors-mes-enlla/" 
  Add-Content -Path .env -Value "API_URL=https://api-media.ccma.cat/pvideo/media.jsp?media=video&versio=vast&idint="
}

py app.py