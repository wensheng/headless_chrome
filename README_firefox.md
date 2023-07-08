# Headless Firefox for Python

## Usage
```python
from headless_firefox import HeadlessFirefox
hlf = HeadlessFirefox()
hlf.get('http://example.com')
hlf.title
print(hlf.src)

```

## Installation:

    pip install headless-firefox

## Dependencies

Firefox is required.

On Ubuntu, non-snap firefox is prefered:

    sudo snap remove firefox
    sudo add-apt-repository ppa:mozillateam/ppa
    sudo apt update
    echo 'Package: *\nPin: release o=LP-PPA-mozillateam\nPin-Priority: 1001'| sudo tee /etc/apt/preferences.d/mozilla-firefox
    sudo apt install firefox

You need to open Firefox normally at least once otherwise it may hang when going headless.
