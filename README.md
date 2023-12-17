# screenshotter

A Python utility that takes a stitched screenshot of a webpage along with individual ones, at any resolution

### Usage

1. Install the package first

```
pip install webscreenshotter.py
```

2. Use the function in your code

```
import take_screenshot from webscreenshotter

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