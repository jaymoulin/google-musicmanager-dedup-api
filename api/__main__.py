import os
from http.server import HTTPServer

from .handler import ApiHandler


def launch_server(hostname, port_number):
    httpd = HTTPServer(
        (hostname, port_number),
        ApiHandler
    )
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    PORT = int(os.getenv("PORT", "80"))
    print("starting service on", PORT)
    launch_server(
        "0.0.0.0",
        PORT,
    )
