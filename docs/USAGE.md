# Usage Guide

## Installation

```bash
pip install git+https://github.com/NetworkSofifi/scrapy-socks5h.git

## Scrapy Settings

```python
DOWNLOADER_MIDDLEWARES = {
  'scrapy_socks5h.socks5h_proxy_middleware.Socks5hProxyMiddleware': 50,
  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

HTTP_PROXY = 'socks5h://10.100.100.1:9050'  # WireGuard Tor Ga

## Verification

Test .onion connectivity using:

```bash
curl --socks5-hostname 10.100.100.1:9050 http://check.torproject.org
