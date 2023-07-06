import os
from io import BytesIO
from zipfile import ZipFile
from stat import S_IXUSR

import requests


last_ver = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').content
with open('./chromedriver_version', 'wb') as f:
    f.write(last_ver)

last_ver = last_ver.decode()
print('Latest version: ' + last_ver)

file_dir_map = {
    'chromedriver_win32.zip': 'windows_amd64',
    'chromedriver_linux64.zip': 'linux_x86_64',
    'chromedriver_mac64.zip': 'mac_x86_64',
    'chromedriver_mac_arm64.zip': 'mac_arm64',
}

for zfile in file_dir_map:
    res = requests.get(f'https://chromedriver.storage.googleapis.com/{last_ver}/{zfile}')
    with ZipFile(BytesIO(res.content)) as z:
        for name in z.namelist():
            outpath = f'./headless_chrome/data/{file_dir_map[zfile]}'
            if not os.path.isdir(outpath):
                os.makedirs(outpath)
            extracted_path = z.extract(name, outpath)
            if not name.startswith('LICENSE'):
                os.chmod(extracted_path, os.stat(extracted_path).st_mode | S_IXUSR)
