import asyncio
from iproxy import loop
from iproxy.spider import cn_proxy_spider

if __name__ == '__main__':
    loop.run_until_complete(asyncio.gather(
        cn_proxy_spider()))
    loop.close()
