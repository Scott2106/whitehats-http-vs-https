import os
import threading
from flask import Flask, render_template, request
from werkzeug.serving import make_server

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"[{request.scheme.upper()} :{request.host.split(':')[-1]}] Username: {username}", flush=True)
        print(f"[{request.scheme.upper()} :{request.host.split(':')[-1]}] Password: {password}", flush=True)
        return render_template("success.html", username=username)
    return render_template("login.html")


def serve(host, port, ssl_context=None):
    server = make_server(host, port, app, threaded=True, ssl_context=ssl_context)
    server.serve_forever()


if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")      
    https_port = int(os.getenv("HTTPS_PORT", 5000))
    http_port = int(os.getenv("HTTP_PORT", 5001))

    # HTTP server in a background thread
    threading.Thread(target=serve, args=(host, http_port), daemon=True).start()
    print(f"HTTP  on port {http_port}", flush=True)

    # HTTPS server in the main thread
    print(f"HTTPS on port {https_port}", flush=True)
    serve(host, https_port, ssl_context=("cert.pem", "key.pem"))