import yaml
import os

CONFIG_FILE = "config.yaml"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"{CONFIG_FILE} not found.")
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)

config = load_config()
