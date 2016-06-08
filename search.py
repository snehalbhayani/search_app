from flask import Flask
app = Flask(__name__)

# Use pyopenssl https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning
try:
    import urllib3.contrib.pyopenssl
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except ImportError:
    pass


if __name__ == "__main__":
    # Send files if this is the main run file
    # Hence probably no webserver
    from flask import send_from_directory

    @app.route('/lib/<path:path>')
    def send_lib(path):
        return send_from_directory('../bower_components', path)

    @app.route('/docroot/<path:path>')
    def send_js(path):
        return send_from_directory('../docroot', path)

    app.run(debug=True, port=5443, ssl_context=("../../misc/server.crt", "../../misc/server.key"))
