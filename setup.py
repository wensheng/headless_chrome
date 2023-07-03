"""
Build wheel package for headless_chrome.

"""
from os.path import dirname, join, abspath
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel


# system = platform.system().lower()
files_to_include = []

class dist_wheel(bdist_wheel):
    def finalize_options(self):
        # Call the parent class's finalize_options method
        super().finalize_options()
        print('#'*80)
        print(self.plat_name)

        # Access the plat_name option and store it in the global variable
        global files_to_include
        if self.plat_name in ['manylinux_2_34_x86_64', 'macosx_x86_64', 'macosx_arm64']:
            files_to_include.append(f'data/{self.plat_name}/chromedriver')
        elif self.plat_name == 'win_amd64':
            files_to_include.append('data/windows/chromedriver.exe')
        else:
            raise ValueError('Unsupported platform: {}'.format(self.plat_name))
        print('#'*80)
        print('files_to_include: {}'.format(files_to_include))


setup_args = {
    'cmdclass': {'bdist_wheel': dist_wheel},
    'name': 'headless_chrome',
    'version': '0.4.10',
    'license': 'Apache 2.0',
    'description': 'headless_chrome for Python, based on Selenium WebDriver',
    'long_description': open(join(abspath(dirname(__file__)), 'README.md')).read(),
    'url': 'https://github.com/wensheng/headless_chrome/',
    'project_urls': {
        'Bug Tracker': 'https://github.com/wensheng/headless_chrome/issues',
    },
    'python_requires': '~=3.8',
    'classifiers': ['Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Operating System :: POSIX',
                    'Operating System :: Microsoft :: Windows',
                    'Operating System :: MacOS :: MacOS X',
                    'Topic :: Software Development :: Libraries'],
    'packages': find_packages(),
    'include_package_data': False,
    'package_data': {'headless_chrome': files_to_include},
    'install_requires': [
    ],
    'zip_safe': False
}

setup(**setup_args)
