import os
import requests
import shutil
from tqdm.auto import tqdm

url = input()
with requests.get(url, stream=True) as r:
    total_length = int(r.headers.get("Content-Length"))
    with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
        with open(f"{os.path.basename(r.url)}", 'wb')as output:
            shutil.copyfileobj(raw, output)
