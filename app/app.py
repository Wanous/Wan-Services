from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from app.config_loader import load_config, save_config
import os
import sys

from app.config_loader import load_config


def create_app():

    # Base path management
    if getattr(sys, "frozen", False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Creation of the app
    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    # Loading configuration
    config = load_config()

    app.config["MEDIA_PATH"] = config.get("media_path", "")
    app.config["PROFILE"] = config.get("profile", "pc")
    app.config["ENABLE_SETTINGS"] = config.get("ui", {}).get("enable_settings", False)

    # Global variables for templates
    @app.context_processor
    def inject_globals():
        return dict(
            enable_settings=app.config["ENABLE_SETTINGS"],
            profile=app.config["PROFILE"]
        )
    
    from app.roads import roads   # To add the roads to the path (after app is initialized)
    app.register_blueprint(roads) # Blueprint to avoid context error

    return app




