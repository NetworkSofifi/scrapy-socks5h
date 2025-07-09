#!/usr/bin/env python
from setuptools import setup, find_packages
from scrapy_socks5h.__version__ import __version__

with open("README.md") as f:
    long_description = f.read()

setup(
    name="scrapy-socks5h",
    description="SOCKS5h middleware for Scrapy with Tor support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sophia Lopez",
    author_email="you@example.com",
    license="MIT",
    url="https://github.com/NetworkSofifi/scrapy-socks5h",
    packages=find_packages(include=["scrapy_socks5h"]),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
