import aiohttp
import aiosocks
from bs4 import BeautifulSoup
from aiosocks.connector import SocksConnector
from . import PROXY_ADDRESS, PROXY_PORT
from ..db import db

async def cn_proxy_spider():
    cn_proxy_url = "http://cn-proxy.com/"
    conn = SocksConnector(proxy=aiosocks.Socks5Addr(
       PROXY_ADDRESS, PROXY_PORT), proxy_auth=None, remote_resolve=True)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(cn_proxy_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'lxml')
            # ['proxy ip', 'proxy port', 'address', 'time']
            ips = []
            tbody = soup.find('tbody')
            for _ in tbody.find_all('tr')[:5]:
                td = _.find_all('td')
                ips.append({
                    'ip'  : td[0].string+':'+td[1].string,
                    'addr': td[2].string.split(" ")[0], # 省份
                    'time': td[-1].string})
                # insert into database
            await db.ips.insert_one({'ips': ips})
