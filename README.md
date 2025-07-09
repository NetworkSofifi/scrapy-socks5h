# scrapy-socks5h

A fork of [PySocks](https://github.com/Anorov/PySocks) focused on supporting `socks5h://` proxies inside Scrapy spiders — with special attention to `.onion` routing and Tor anonymity.

## Features

- SOCKS5h support inside Scrapy
- Fully DNS-leaking safe `.onion` crawling
- Middleware-ready architecture for Scrapy 2.13+
- WireGuard + Tor gateway testing environment

## Usage
- Refer to https://github.com/NetworkSofifi/debian-tor-gateway for WireGuard tunnel setup.
```python
meta = {
    'proxy': 'socks5h://10.100.100.1:9050'
}
