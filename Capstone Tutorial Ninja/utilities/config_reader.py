import configparser
import os

config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "config.ini"
)

config.read(config_path)

def get_url():
    return config.get("settings", "url")

def get_browser():
    return config.get("settings", "browser")

def get_implicit_wait():
    return int(config.get("settings", "implicit_wait"))

def get_explicit_wait():
    return int(config.get("settings", "explicit_wait"))
