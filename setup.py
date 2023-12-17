from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='webscreenshotter',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        "selenium"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
