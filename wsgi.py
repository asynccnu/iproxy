import sys
from iproxy import web, app, loop

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    web.run_app(app, host=host, port=port)
