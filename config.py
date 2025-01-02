import json
import os

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "min_repeats_range": 900,
    "max_repeats_range": 1000,
    "min_total_steps_range": 2500,
    "max_total_steps_range": 4000,
    "default_batch_size": 2
}

def load_config():
    """Loads configuration from config.json or creates it with defaults."""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                return config
        else:
            save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
    except Exception as e:
        print(f"Error loading config: {e}")
        return DEFAULT_CONFIG


def save_config(config):
    """Saves configuration to config.json."""
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")