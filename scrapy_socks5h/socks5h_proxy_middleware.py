# socks5h_proxy_middleware.py

class Socks5hProxyMiddleware:
    def __init__(self, proxy_url):
        self.proxy_url = proxy_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(proxy_url=crawler.settings.get("SOCKS5H_PROXY", None))

    def process_request(self, request, spider):
        if ".onion" in request.url:
            if self.proxy_url:
                request.meta["proxy"] = self.proxy_url
                spider.logger.debug(f"[socks5h_proxy] Routing .onion traffic through {self.proxy_url}")
