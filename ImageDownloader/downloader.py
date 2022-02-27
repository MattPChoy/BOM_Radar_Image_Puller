import os
import time
import datetime
from ftplib import FTP

def get_brisbane_filenames(filename):
    if filename.startswith("IDR663.T."):
        brisbane_filenames.append(filename)

def ftp_download_image():
    ftp = FTP(r"ftp.bom.gov.au")
    ftp.login()
    ftp.cwd("/anon/gen/radar")

    ftp.retrlines("NLST", get_brisbane_filenames)

    for filename in brisbane_filenames:
        if not os.path.isfile(filename):
            with open(filename, "wb") as fp:
                ftp.retrbinary(f"RETR {filename}", fp.write)
                print(f"Downloaded and saved {filename}")
    ftp.quit

if __name__ == "__main__":
    # download_image_3("http://www.bom.gov.au/radar/IDR663.T.202202252249.png")
    while 1:
        brisbane_filenames = []
        ftp_download_image()
        print(f"Downloading images complete at {datetime.datetime.now()}")
        time.sleep(1800) # 30 mins
        # time.sleep(30)
