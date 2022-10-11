import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup



def app():

  load_dotenv()
  url_base = requests.get(os.getenv('URL_BASE'))
  html_page = ''


  def page_parser(page: str):
    return BeautifulSoup(page, "html.parser")

  def get_chapter_url(page: str):
    print(page.find_all("li", class_= "C-llistatVideo"))
    return  

  html_page = page_parser(url_base.content)
  get_chapter_url(html_page)  


app()

