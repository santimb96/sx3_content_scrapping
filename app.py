import os
import requests
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def app():

    load_dotenv()
    URL_BASE = requests.get(os.getenv('URL_BASE'))
    API_URL = os.getenv('API_URL')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
    html_page = ''
    chapters_list = ''
    video_id = []
    videos = []

    def page_parser(page):
        return BeautifulSoup(page, "html.parser")

    def get_chapter_url(page):
        return page.find_all("li", class_="C-llistatVideo")

    def get_media_links(list):
        for chapter in list:
            for link in chapter.findAll("a"):
                video_id.append(link.get("href").split("/")[7])
        return

    def get_data_from_link(ids):
        for id in ids:
            req = requests.get(f"{API_URL}{id}", headers=headers)
            data = json.loads(req.text)
            videos.append(data["media"]["url"][0]["file"])

        return
        
    html_page = page_parser(URL_BASE.content)
    chapters_list = get_chapter_url(html_page)
    get_media_links(chapters_list)
    get_data_from_link(video_id)


app()
