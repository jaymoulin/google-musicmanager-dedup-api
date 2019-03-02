from http.server import BaseHTTPRequestHandler
import os
import sqlite3
from urllib.parse import urlparse, parse_qs
from cgi import parse_header, parse_multipart


def _get_connection() -> sqlite3.Connection:
    db_path = os.getenv("DB_PATH", "/app/db/googlemusicmanager.db")
    db_exists = os.path.isfile(db_path)
    if not db_exists:
        basedir = os.path.dirname(db_path)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        open(db_path, 'a').close()
    connection = sqlite3.connect(db_path)
    if not db_exists:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE path (date text, path text)')
        connection.commit()

    return connection


_connection = _get_connection()


class ApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self._get_path()
        cursor = _connection.cursor()
        cursor.execute('SELECT count(*) FROM path WHERE path=?', path)
        result = cursor.fetchone()[0]
        self.send_response(404 if result == 0 else 204)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        path = self._get_path()
        cursor = _connection.cursor()
        cursor.execute('INSERT INTO path (path, "date") VALUES (?, date("now"))', path)
        _connection.commit()
        self.send_response(204)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_DELETE(self):
        path = self._get_path()
        cursor = _connection.cursor()
        cursor.execute('DELETE FROM path WHERE path=?', path)
        _connection.commit()
        self.send_response(204)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def _get_path(self):
        query_components = parse_qs(urlparse(self.path).query)
        path = query_components.get("path")
        if not path:
            postvars = self._parse_POST()
            path = (postvars[b'path'][0].decode('utf-8'),)
        return path

    def _parse_POST(self):
        ctype, pdict = parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        return postvars
