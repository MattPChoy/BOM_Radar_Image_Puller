import requests
import shutil
import urllib.request as req
from contextlib import closing

sources = {
    "QLD_Mt_Stapylton_128", "http://www.bom.gov.au/radar/IDR663.T.202202252249.png"
}

def download_image(url):
    img_data = requests.get(url).content
    with open('image_name.png', 'wb') as handler:
        handler.write(img_data)

def download_image_2(url):
    with open('image_name.png', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

def download_image_3(url):
    response = requests.get(url)
    if not response.ok:
        print(response)
    file = open("image_name.png", "wb")
    file.write(response.content)
    file.close()

def download_image_4(url):
    # Downloading from an FTP stream
    with closing(req.urlopen(url)) as r:
        with open('image_name.png', 'wb') as f:
            shutil.copyfileobj(r, f)

if __name__ == "__main__":
    # download_image_3("http://www.bom.gov.au/radar/IDR663.T.202202252249.png")
    download_image_4('ftp://ftp.bom.gov.au/anon/gen/radar/')
