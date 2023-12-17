from webscreenshotter import take_screenshot

if __name__ == "__main__":
    take_screenshot (
        "https://en.wikipedia.org/wiki/qr_code",
        width=1280, height=720,
        directory=".screencaps", file_suffix="capture_",
        stitch=True
    )