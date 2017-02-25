import os
from aiohttp import web
from aiohttp.web import Response
from ..spider import cn_proxy_spider
from ..db import db

api = web.Application()

# ====== async view handlers ======
async def index(request):
    return web.json_response({'hello': 'world'})

async def get_iproxy(request):
    cursor = db.ips.find()
    _ips = await cursor.to_list(length=100) # 100个ip, 可用IP: 5个
    ips = _ips[0].get('ips')
    return web.json_response({'ips': ips})

def ping_ip(ip=None):
    ping_cmd = 'ping -c 2 %s' % ip
    ping_result = os.popen(ping_cmd).read() # block
    return ping_result

def check_ip(ips, ip_use):
    cnt = 0; _ip_use = []
    for ip in ips:
        ping_result = ping_ip(ip.get('ip').split(':')[0])
        if ping_result.find('100% packet loss') < 0:
            cnt+=1; _ip_use.append(ip)
            if (cnt == ip_use): break
    return _ip_use

async def start_spider(request):
    query_string = request.rel_url.query_string
    if query_string:
        k = []; v = []
        for _ in query_string.split('&'):
            k.append(_.split('=')[0])
            v.append(_.split('=')[1])
        args = dict(zip(k, v))
        ip_all = int(args.get('ip_all'))
        ip_use = int(args.get('ip_use'))
    else: # 404: need query string **in here**
        return Response(body = b'{}',
        content_type = 'application/json', status = 404)
    # 爬取指定数量IP
    ips = await cn_proxy_spider(ip_all);
    # 检测指定数量的可用IP(ping)
    _ip_use = check_ip(ips, ip_use) # block the eventloop
    # 清空数据库
    await db.ips.drop()
    # 放入数据库
    await db.ips.insert_one({'ips': _ip_use})
    return web.json_response({'ips': _ip_use})
# =================================

# ====== url --------- maps  ======
# index
api.router.add_route('GET', '/', index, name='index')
# management
# -- 1. 清空数据库
# -- 2. 爬取指定数量IP并检测
# -- 3. 检测指定数量的可用IP放入数据库
api.router.add_route('GET', '/start_spider/', start_spider, name='start_spider')
# use
# -- 随机获取一个可用IP
api.router.add_route('GET', '/ip/', get_iproxy, name='get_iproxy')
# =================================
