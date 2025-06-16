import requests

def download_file(url: str, filepath: str) -> None:
    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as f:
        f.write(response.content)