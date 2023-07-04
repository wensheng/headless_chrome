import os
from platform import system, machine

from .chrome.options import Options as ChromeOptions  # noqa
from .chrome.service import Service as ChromeService  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.keys import Keys  # noqa
from .common.proxy import Proxy  # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.by import By
from .version import __version__


def headless_chrome():
    """
    chromedriver path:
    - Windows_amd64: ./data/windows_amd64/chromedriver.exe
    - Linux_x86_64: ./data/linux_x86_64/chromedriver
    - Mac_x86_64: ./data/mac_x86_64/chromedriver
    - Mac_arm64: ./data/mac_arm64/chromedriver
    Other architectures are not supported.
    """
    options = ChromeOptions()
    system_name = system().lower()
    machine_name = machine().lower()
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    if system_name == 'darwin':
        driver_path = os.path.join(parent_dir, 'data', f'mac_{machine_name}', 'chromedriver')
    elif system_name == 'windows' and machine_name == 'amd64':
        driver_path = os.path.join(parent_dir, 'data', f'windows_amd64', 'chromedriver.exe')
    elif system_name == 'linux' and machine_name == 'x86_64':
        driver_path = os.path.join(parent_dir, 'data', 'linux_x86_64', 'chromedriver')
    else:
        raise Exception(f'Unsupported system: {system_name} {machine_name}')
    service = ChromeService(driver_path)
  
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
  
    return Chrome(service=service, options=options)
  

# We need an explicit __all__ because the above won't otherwise be exported.
__all__ = [
    'Chrome',
    'ChromeOptions',
    'ChromeService',
    'Remote',
    'DesiredCapabilities',
    'ActionChains',
    'Proxy',
    'Keys',
    'By',
    'headless_chrome',
]
