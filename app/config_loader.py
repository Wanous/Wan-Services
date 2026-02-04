import json
import os
import sys
from pathlib import Path

# ------------------------------
#        CONFIG MANAGER (loader)
# ------------------------------

"""
File to Externalized User Configuration 

The application copies a default configuration on first launch then modify the file for 
all user changes in an OS-specific application data directory.

The path for each OS :
    Windows	   %APPDATA%/WanServices/config.json
    Linux 	   ~/.config/wanservices/config.json
    macOS	   ~/Library/Application Support/WanServices/config.json

"""

APP_NAME = "WanServices" # Name of the folder 


def get_user_config_dir():
    """Get the OS-specific application data directory the user is on"""
    if sys.platform.startswith("win"):                      # Windows
        return Path(os.getenv("APPDATA")) / APP_NAME  
    elif sys.platform == "darwin":                          # Apple
        return Path.home() / "Library" / "Application Support" / APP_NAME
    else:                                                   # Linux
        return Path.home() / ".config" / APP_NAME


def get_default_config_path():
    """Get the default config data from the executable (store with pyinstaller. See WanServices.spec --> datas)"""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "config.json"
    return Path("config.json")


def get_user_config_path():
    """Return the completed path to the configuration file"""
    config_dir = get_user_config_dir()
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir / "config.json"


def load_config():
    """Load the configuration"""
    user_config = get_user_config_path()

    if not user_config.exists():
        default_config = get_default_config_path()
        user_config.write_text(default_config.read_text(), encoding="utf-8")

    with open(user_config, "r", encoding="utf-8") as f:
        return json.load(f)


def save_config(data: dict):
    """Save the configuration to the user config folder"""
    with open(get_user_config_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
