import os
from distutils.util import get_platform

from .chrome.options import Options as ChromeOptions  # noqa
from .chrome.service import Service as ChromeService  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.keys import Keys  # noqa
from .common.proxy import Proxy  # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.by import By

__version__ = '4.10.0'

def headless_chrome():
    options = ChromeOptions()
    platform = get_platform().replace('-', '_')
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    if platform.startswith('win'):
        driver_path = os.path.join(parent_dir, 'data', 'windows', 'chromedriver.exe')
    else:
        driver_path = os.path.join(parent_dir, 'data', platform, 'chromedriver')
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
