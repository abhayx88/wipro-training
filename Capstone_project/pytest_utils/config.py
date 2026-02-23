import configparser
import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.ini"
REPORTS_DIR = PROJECT_ROOT / "reports" / "pytest"

config = configparser.ConfigParser()
config.read(CONFIG_PATH, encoding="utf-8")

BASE_URL = os.getenv("URL", config.get("app", "base_url", fallback="https://tutorialsninja.com/demo/"))
BROWSER = os.getenv("BROWSER", config.get("app", "browser", fallback="chrome")).strip().lower()
TIMEOUT = int(os.getenv("TIMEOUT", config.get("app", "timeout", fallback="10")))
