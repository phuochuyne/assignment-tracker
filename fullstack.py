"""Runnable full-stack entry point for Assignment Tracker."""

from pathlib import Path

from flask import send_file

from backend import create_app as create_backend_app


PROJECT_ROOT = Path(__file__).resolve().parent
FRONTEND_ROOT = PROJECT_ROOT / "frontend"


def create_app(testing: bool = False):
    app = create_backend_app(testing=testing)

    @app.get("/")
    def frontend_index():
        return send_file(FRONTEND_ROOT / "index.html", mimetype="text/html")

    @app.get("/app.css")
    def frontend_css():
        return send_file(FRONTEND_ROOT / "app.css", mimetype="text/css")

    @app.get("/app.js")
    def frontend_javascript():
        return send_file(FRONTEND_ROOT / "app.js", mimetype="text/javascript")

    return app
