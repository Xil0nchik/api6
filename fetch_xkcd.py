import requests
import random
from download_utils import download_file

def fetch_random_xkcd_comic(filepath: str) -> str:
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    latest_num = response.json().get("num")

    random_num = random.randint(1, latest_num)
    url = f"https://xkcd.com/{random_num}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic_data = response.json()

    img_url = comic_data.get("img")
    alt_text = comic_data.get("alt") or ""

    download_file(img_url, filepath)
    return alt_text