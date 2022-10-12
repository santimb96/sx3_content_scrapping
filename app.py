from msilib.schema import Patch
import os
import requests
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def app():

    load_dotenv()

    URL_BASE = requests.get(os.getenv("URL_BASE"))
    API_URL = os.getenv("API_URL")
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    html_page = ""
    chapters_list = ""
    video_id = []
    videos = []

    def page_parser(page):
        return BeautifulSoup(page, "html.parser")

    def get_chapter_url(page):
        return page.find_all("li", class_="C-llistatVideo")

    def get_media_links(list):
        for chapter in list:
            link = chapter.findAll("a")
            video_id.append(link[0]["href"].split("/")[7])
        return

    def get_data_from_link(ids=[]):

        if len(ids):
            for id in ids:
                try:
                    req = requests.get(f"{API_URL}{id}", headers=headers)
                    data = json.loads(req.text)
                    videos.append(
                        {
                            "title": data["informacio"]["titol"],
                            "url": data["media"]["url"][0]["file"],
                        }
                    )
                except:
                    raise Exception("¡Something went wrong!")
        else:
            print("¡The video's id list is empty!")
            return quit()
        return

    def check_drive_exist(drive):
        return os.path.exists(drive + ":\\")

    def download_videos(videos):
        directory = "E:\\" if check_drive_exist("e") else "C:\\"
        path = os.path.join(directory, "videos")

        if not os.path.exists(path):
            os.mkdir(path)

        for index, video in enumerate(videos):
            file_name = str(index) + "-" + video["title"] + ".mp4"
            file_path = os.path.join(path, file_name)

            if not os.path.exists(file_path):
                
                req = requests.get(video["url"], stream=True)
                print("The file doesn't exist ---> Downloading " + video["title"])
    
                with open(file_path, "wb") as f:
                 for chunk in req.iter_content(chunk_size=1024 * 1024):
                     if chunk:
                         f.write(chunk)
    
                print("File downloaded!")

        return print("¡All files downloaded!")

    html_page = page_parser(URL_BASE.content)
    chapters_list = get_chapter_url(html_page)
    get_media_links(chapters_list)
    get_data_from_link(video_id)
    download_videos(videos)


app()
