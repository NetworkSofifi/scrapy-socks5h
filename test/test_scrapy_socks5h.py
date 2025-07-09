def test_middleware_import():
    from scrapy_socks5h.socks5h_proxy_middleware import Socks5hProxyMiddleware
    assert Socks5hProxyMiddleware is not None
