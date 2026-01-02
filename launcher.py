import sys
import time
import threading

from app.app import create_app
from app.config_loader import load_config


def run_server():
    config = load_config()
    server_cfg = config.get("server", {})

    host = server_cfg.get("host", "127.0.0.1")
    port = server_cfg.get("port", 5000)

    print("\n===================================")
    print(" Wan'Services server starting")
    print(f" Host : {host}")
    print(f" Port : {port}")
    print(" Press Ctrl+C to stop")
    print("===================================")

    app = create_app()

    app.run(
        host=host,
        port=port,
        debug=False,
        use_reloader=False
    )

if __name__ == "__main__":
    run_server()


