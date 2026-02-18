import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


def get_url():
    return config["DEFAULT"]["url"]


def get_browser():
    return config["DEFAULT"]["browser"]


def get_explicit_wait():
    return int(config["DEFAULT"]["explicit_wait"])
