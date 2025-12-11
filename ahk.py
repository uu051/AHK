import re
import requests

def download_drive(url, output):
    file_id_match = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if not file_id_match:
        raise ValueError("Не удалось получить ID файла из ссылки.")
    
    file_id = file_id_match.group(1)
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    
    session = requests.Session()
    response = session.get(download_url, stream=True)

    for key, val in response.cookies.items():
        if key.startswith("download_warning"):
            response = session.get(download_url, params={"confirm": val}, stream=True)
            break

    with open(output, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

download_drive("https://drive.google.com/file/d/1EqwGcRGOWr15o6Gv-zKRW7HqEVxc7cHL/view?usp=sharing", "ПРВ V2.ahk")