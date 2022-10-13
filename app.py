import os
import requests
import json
from colorama import Fore
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def app():

    load_dotenv()

    URL_BASE = os.getenv("URL_BASE")
    API_URL = os.getenv("API_URL")
    page_response = requests.get(URL_BASE)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    html_page = ""
    chapters_list = ""
    video_id = []
    videos = []

    def check_status_code(status_code):
        if status_code == 200:
            return
        else:
            print(f"{Fore.RED}{status_code}: forbidden access")
            return quit()

    def page_parser(page):
        return BeautifulSoup(page, "html.parser")

    def get_chapter_url(page):
        return page.find_all("li", class_="C-llistatVideo")

    def get_media_links(list_of_chapters):
        for chapter in list_of_chapters:
            link = chapter.findAll("a")
            video_id.append(link[0]["href"].split("/")[7])
        return

    def get_folder_name(url):
        return url.split("/")[5]

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
        directory = "E:/" if check_drive_exist("e") else "C:/"
        path = os.path.join(directory, f"videos/{get_folder_name(URL_BASE)}")

        if not os.path.exists(path):
            os.makedirs(path)

        for index, video in enumerate(videos):
            file_name = str(index + 1) + "-" + video["title"] + ".mp4"
            file_path = os.path.join(path, file_name)

            if not os.path.exists(file_path):

                req = requests.get(video["url"], stream=True)
                print(f"{Fore.BLUE}The file doesn't exist in your folder!")
                print(Fore.GREEN + "Downloading " + video["title"])

                with open(file_path, "wb") as f:
                    for chunk in req.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            f.write(chunk)

                print("File downloaded!")

        return print("¡All files downloaded!")

    check_status_code(page_response.status_code)
    html_page = page_parser(page_response.content)
    chapters_list = get_chapter_url(html_page)
    get_media_links(chapters_list)
    get_data_from_link(video_id)
    download_videos(videos)


app()
