sslocal -c shadowsocks.json -d start
echo "===== aiohttp server start on 0.0.0.0:8080 ====="
python wsgi.py 0.0.0.0 8080
