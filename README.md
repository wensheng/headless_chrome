# Headless Chrome for Python

**(See [README_firefox.md](README_firefox.md) for Headless Firefox)**

## Usage

```python
from headless_chrome import HeadlessChrome
hlc = HeadlessChrome()
hlc.get('http://example.com')
hlc.title
print(hlc.src)
```

## Installation:

    pip install headless-chrome

## Dependencies

Google Chrome is required.

On Ubuntu Linux, you can install it by:

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dkpg -i google-chrome-stable_current_amd64.deb


