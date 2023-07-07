"""
HeadlessFirefox wraps a headless GeckoDriver inside the Selenium webdriver.
"""
import os
from platform import system, machine

from .firefox.options import Options as FirefoxOptions
from .firefox.service import Service as FirefoxService
from .firefox.webdriver import WebDriver as Firefox
from .common.action_chains import ActionChains  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.keys import Keys  # noqa
from .common.proxy import Proxy  # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.by import By
from .version import __version__


class HeadlessFirefoxException(Exception):
    """
    Exception for HeadlessFirefox
    """


class HeadlessFirefox(Firefox):
    """
    geckodriver path:
    - Windows_amd64: ./data/windows_amd64/geckodriver.exe
    - Linux_x86_64: ./data/linux_x86_64/geckodriver
    - Mac_x86_64: ./data/mac_x86_64/geckodriver
    - Mac_arm64: ./data/mac_arm64/geckodriver
    Other architectures are not supported.
    """
    def __init__(self, *args, **kwargs):
        if 'options' not in kwargs:
            kwargs['options'] = FirefoxOptions()
        if not isinstance(kwargs['options'], FirefoxOptions):
            raise HeadlessFirefoxException('options must be an instance of FirefoxOptions')

        kwargs['options'].add_argument('--headless')
        kwargs['options'].add_argument('--window-size=1920,1080')

        system_name = system().lower()
        machine_name = machine().lower()
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        if system_name == 'darwin':
            driver_path = os.path.join(parent_dir, 'data', f'mac_{machine_name}', 'geckodriver')
        elif system_name == 'windows' and machine_name == 'amd64':
            driver_path = os.path.join(parent_dir, 'data', 'windows_amd64', 'geckodriver.exe')
        elif system_name == 'linux' and machine_name == 'x86_64':
            driver_path = os.path.join(parent_dir, 'data', 'linux_x86_64', 'geckodriver')
        elif system_name == 'linux' and machine_name == 'arm64':
            driver_path = os.path.join(parent_dir, 'data', 'linux_arm64', 'geckodriver')
        else:
            raise HeadlessFirefoxException(f'Unsupported system: {system_name} {machine_name}')
        kwargs['service'] = FirefoxService(driver_path)

        super().__init__(*args, **kwargs)

    @property
    def src(self):
        """
        for convience, alias for page_source
        """
        return self.page_source


# We need an explicit __all__ because the above won't otherwise be exported.
__all__ = [
    'Firefox',
    'FirefoxOptions',
    'FirefoxService',
    'Remote',
    'DesiredCapabilities',
    'ActionChains',
    'Proxy',
    'Keys',
    'By',
    'HeadlessFirefox',
]
