import os
import sys
import tarfile
from io import BytesIO
from zipfile import ZipFile
from stat import S_IXUSR

import requests


res = requests.get('https://github.com/mozilla/geckodriver/releases/latest')
# url will be redirected to https://github.com/mozilla/geckodriver/releases/tag/[version]
geckodriver_version = res.url.split('/')[-1]

with open('./geckodriver_version', 'w') as f:
    f.write(geckodriver_version)

print('Latest version: ' + geckodriver_version)

file_dir_map = {
    'win64.zip': 'windows_amd64',
    'linux64.tar.gz': 'linux_x86_64',
    'linux-aarch64.tar.gz': 'linux_arm64',
    'macos.tar.gz': 'mac_x86_64',
    'macos-aarch64.tar.gz': 'mac_arm64',
}

for zfile in file_dir_map:
    url = f'https://github.com/mozilla/geckodriver/releases/download/{geckodriver_version}/geckodriver-{geckodriver_version}-{zfile}'
    res = requests.get(url)
    if url.endswith('.tar.gz'):
        with tarfile.open(fileobj=BytesIO(res.content)) as tar:
            for member in tar.getmembers():
                if member.isfile():
                    member.name = os.path.basename(member.name)
                    tar.extract(member, f'./headless_firefox/data/{file_dir_map[zfile]}')
    elif url.endswith('.zip'):
        with ZipFile(BytesIO(res.content)) as z:
            for name in z.namelist():
                outpath = f'./headless_firefox/data/{file_dir_map[zfile]}'
                if not os.path.isdir(outpath):
                    os.makedirs(outpath)
                extracted_path = z.extract(name, outpath)
                if not name.startswith('LICENSE'):
                    os.chmod(extracted_path, os.stat(extracted_path).st_mode | S_IXUSR)
    else:
        print('Unknown file format: ' + url)
