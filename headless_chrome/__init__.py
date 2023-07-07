"""
HeadlessChrome wraps a headless ChromeDriver inside the Selenium webdriver.
"""
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


class HeadlessChromeException(Exception):
    """
    Exception for HeadlessChrome
    """


class HeadlessChrome(Chrome):
    """
    chromedriver path:
    - Windows_amd64: ./data/windows_amd64/chromedriver.exe
    - Linux_x86_64: ./data/linux_x86_64/chromedriver
    - Mac_x86_64: ./data/mac_x86_64/chromedriver
    - Mac_arm64: ./data/mac_arm64/chromedriver
    Other architectures are not supported.
    """
    def __init__(self, *args, **kwargs):
        if 'options' not in kwargs:
            kwargs['options'] = ChromeOptions()
        if not isinstance(kwargs['options'], ChromeOptions):
            raise HeadlessChromeException('options must be an instance of ChromeOptions')

        if 'headless' in kwargs:
            if not kwargs['headless']:
                kwargs['options'].add_argument('--headless=new')
            del kwargs['headless']
        else:
            kwargs['options'].add_argument('--headless=new')
        kwargs['options'].add_argument('--window-size=1920,1080')
        kwargs['options'].add_argument('--disable-gpu')
        kwargs['options'].add_argument('--ignore-certificate-errors')
        kwargs['options'].add_argument('--disable-extensions')
        kwargs['options'].add_argument('--no-sandbox')
        kwargs['options'].add_argument('--disable-dev-shm-usage')

        system_name = system().lower()
        machine_name = machine().lower()
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        if system_name == 'darwin':
            driver_path = os.path.join(parent_dir, 'data', f'mac_{machine_name}', 'chromedriver')
        elif system_name == 'windows' and machine_name == 'amd64':
            driver_path = os.path.join(parent_dir, 'data', 'windows_amd64', 'chromedriver.exe')
        elif system_name == 'linux' and machine_name == 'x86_64':
            driver_path = os.path.join(parent_dir, 'data', 'linux_x86_64', 'chromedriver')
        else:
            raise HeadlessChromeException(f'Unsupported system: {system_name} {machine_name}')
        kwargs['service'] = ChromeService(driver_path)

        super().__init__(*args, **kwargs)

    @property
    def src(self):
        """
        for convience, alias for page_source
        """
        return self.page_source


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
    'HeadlessChrome',
]
