# webscreenshotter

A Python utility that takes a stitched screenshot of a webpage along with individual ones, at any resolution

### Usage

1. Install the package first

```
pip install webscreenshotter
```

2. Use the function in your code

```
from webscreenshotter import take_screenshot

if __name__ == "__main__":
    take_screenshot (
        "https://en.wikipedia.org/wiki/qr_code",
        width=1280, height=720,
        directory=".screencaps", file_suffix="capture_",
        stitch=True
    )
```

Change the directory and suffix to whatever you want.

3. Inspect the location you set as output directory for screenshot

Notes:

1. Stitching happens vertically.
2. Setting different resolutions can result in different style webpages, especially with PWAs and mobile-optimized webpages.

# License
[GPLv3 License](LICENSE)

By 0x4f (Owais Shaikh)

https://pypi.org/project/webscreenshotter/
https://github.com/0x4f53/webscreenshotter