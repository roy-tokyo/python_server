from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import sys, json
import os.path
import glob

class Handler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.make_data()
    def do_GET(self):
        self.make_data()

    def make_data(self):

        #リクエスト情報
        print('path = {}'.format(self.path))

        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)))

        print('\r\n【headers】\r\n-----\r\n{}-----'.format(self.headers))

        if self.path == "/test.zip":
        #zipファイル処理
            self.do_zip_service()
        else:
        #jsonファイル処理
            service_names = []
            files = glob.glob('./*.json')
            for file in files:
                basename = os.path.basename(file)
                service_names.append(os.path.splitext(basename)[0])

            foundFlag = 0

            for name in service_names:
                if self.path == ('/' + name):
                    foundFlag = 1
                    self.do_json_service(name)

            if foundFlag == 0:        
                self.do_notfound()
    
    def do_zip_service(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/zip')
        self.end_headers()
        with open("./test.zip", 'rb') as f:
            self.wfile.write(f.read())

    def do_json_service(self, name):
        f = open(name + ".json")
        result_json = json.load(f)
        f.close()

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result_json).encode('UTF-8'))

    def do_notfound(self):
        f = open("notfound.json")
        result_json = json.load(f)
        f.close()

        self.send_response(404)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result_json).encode('UTF-8'))

PORT = 8888

httpd = HTTPServer(("", PORT), Handler)
httpd.serve_forever()
