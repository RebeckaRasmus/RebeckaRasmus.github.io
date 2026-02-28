"""
Simple Flask server for the wedding website.
Install: pip install flask
Run:     python server.py
"""

from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n💒 Bröllopswebben körs på http://localhost:{port}\n")
    app.run(debug=True, port=port)
