from aiohttp import web
from aiohttp.web import Response
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
# =================================

# ====== url --------- maps  ======
api.router.add_route('GET', '/', index, name='index')
api.router.add_route('GET', '/ip/', get_iproxy, name='get_iproxy')
# =================================
