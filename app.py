import sys
import os
import requests
import json
import platform
from colorama import Fore
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from clint.textui import progress
from time import sleep

"""Function where we placed all functions and variables"""
load_dotenv()
BASE_URL: str = os.getenv("BASE_URL")
API_URL: str = os.getenv("API_URL")
LIMIT: int = 50
LINE_CLEAR: str = "\x1b[2K"
LINE_UP: str = "\033[1A"
page_response: str = ""
headers: dict = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}
html_page: str = ""
chapters_list: str = ""
path: str = ""
video_id: list = []
videos: list = []
attempts: int = 0


def check_status_code(status_code):
    """Checks if the status code is 200 (ok)
    Args:
        status_code (integer): _description_
    Returns:
        bool: return True if code is equal to 200, if not, False
    """
    global attempts
    attempts += 1
    print(
        f"{Fore.CYAN}---> Attempts to download the data from the page ---> {str(attempts)}/{LIMIT}",
        end="\r",
    )
    return status_code == 200


def get_page_data():
    while True:
        res: object = requests.get(BASE_URL)
        if check_status_code(res.status_code):
            global page_response
            page_response = res
            print("\n")
            break
        if attempts == LIMIT:
            print(
                f"{Fore.RED} Timeout! It has been impossible to access the web data. Try later!"
            )
            return quit()
        sleep(2)


def page_parser(page):
    """Receives a page to be parsed
    Args:
        page (Any): response from the request page
    Returns:
        BeautifulSoup: parsed page
    """
    return BeautifulSoup(page, "html.parser")


def get_chapter_url(page):
    """Get the list of chapters from the tv serie
    Args:
        page (BeautifulSoup): parsed page
    Returns:
        List: list of chapters (li elements with links to chapters)
    """
    return page.find_all("li", class_="C-llistatVideo")


def get_media_links(chapter_list):
    """We obtain the video id from every link in chapter_list
    Args:
        chapter_list (List): chapter list
    """
    # los vídeos se cuelgan de más a menos reciente, por lo que no están ordenados cronológicamente y hay que hacer un reverse()
    chapter_list.reverse()
    for chapter in chapter_list:
        link: list = chapter.findAll("a")
        video_id.append(link[0]["href"].split("/")[7])
    return


def get_folder_name(url):
    """Get folder name from tv serie title
    Args:
        url (string): tv serie url
    Returns:
        string: folder name
    """
    return url.split("/")[5]


def get_data_from_link(ids=[]):
    """Get chapter data from every video id code
    Args:
        ids (list, optional): video id list. Defaults to [].
    Raises:
        Exception: return error if we can not get the video data
    Returns:
        NoReturn: quit from the program
    """
    if len(ids):
        for id in ids:
            try:
                res: object = requests.get(f"{API_URL}{id}", headers=headers)
                data: object = json.loads(res.text)
                videos.append(
                    {
                        "title": data["informacio"]["titol"],
                        "url": data["media"]["url"][0]["file"],
                    }
                )
            except:
                raise Exception("¡Something went wrong!")
    else:
        print(f"{Fore.RED}¡The video's id list is empty!")
        return quit()
    return


def check_os_and_return_path(folder_name, windows_base_path, linux_base_path):
    """Check if the OS is Windows or Linux and the returns a path
    Returns:
        string: return path
    """
    if platform.system() == "Windows":
        return os.path.join(
            windows_base_path,
            f"videos/{folder_name}",
        )
    return os.path.join(linux_base_path, str({folder_name}))


def check_drive_exist(drive):
    """Check if disk exists in our system
    Args:
        drive (string): drive letter
    Returns:
        bool: return True or False if the disk exists or not
    """
    return os.path.exists(drive + ":\\")


def download_videos(path, videos):
    """From the the videos list, the program download every chapter
    Args:
        videos (list): list of videos in JSON format
    Raises:
        Exception: return error if any problem appears
    """
    if not os.path.exists(path):
        os.makedirs(path)
    for index, video in enumerate(videos):
        file_name: str = f"{index + 1}-{video['title'].replace(':', '-')}.mp4"
        file_path: str = f"{path}/{file_name}"
        if not os.path.exists(file_path):
            try:
                res: object = requests.get(video["url"], stream=True)
                print(f"{Fore.BLUE}The file doesn't exist in your folder!")
                print(f"{Fore.GREEN}Downloading ---> {video['title']}")

                with open(file_path, "wb") as f:
                    total_size = int(res.headers.get("Content-Length"))
                    for chunk in progress.bar(
                        res.iter_content(chunk_size=1024),
                        expected_size=(total_size / 1024) + 1,
                    ):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                print("File downloaded!")
            except:
                raise Exception("Something went wrong with the download!")
    return print("Are you up to date!")


def main():
    get_page_data()
    html_page = page_parser(page_response.content)
    chapters_list = get_chapter_url(html_page)
    path = check_os_and_return_path(
        get_folder_name(BASE_URL),
        "E:/" if check_drive_exist("e") else f"{os.path.expanduser('~')}/Videos",
        f"{os.path.expanduser('~')}/Videos",
    )

    get_media_links(chapters_list)
    get_data_from_link(video_id)
    download_videos(path, videos)


if __name__ == "__main__":
    main()
