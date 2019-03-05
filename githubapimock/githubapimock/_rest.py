import contextlib
import requests
from flask import jsonify
from threading import Thread


class MockServer(Thread):
    def __init__(self, port=5000):
        super().__init__()
        from flask import Flask
        self.port = port
        self.app = Flask('githubapimock')
        self.url = "http://0.0.0.0:%s" % self.port

        self.app.add_url_rule("/shutdown", view_func=self._shutdown_server)

    def _shutdown_server(self):
        from flask import request
        if not 'werkzeug.server.shutdown' in request.environ:
            raise RuntimeError('Not running the development server')
        request.environ['werkzeug.server.shutdown']()
        return 'Server shutting down...'

    def shutdown_server(self):
        requests.get("http://localhost:%s/shutdown" % self.port)
        self.join()

    def add_callback_response(self, url, callback, methods=('GET',)):
        self.app.add_url_rule(url, view_func=callback, methods=methods)

    def add_json_response(self, url, serializable, methods=('GET',)):
        def callback():
            return jsonify(serializable)

        self.add_callback_response(url, callback, methods=methods)

    def run(self):
        self.app.run(port=self.port)



@contextlib.contextmanager
def rest(addr, port):
    server = MockServer(port=8002)
    server.start()
    server.add_json_response("/json", dict(hello="welt"))
    response = requests.get(server.url + "/json")
    assert 200 == response.status_code
    assert 'hello' in response.json()
    assert 'welt' == response.json()['hello']

    yield

    server.shutdown_server()
