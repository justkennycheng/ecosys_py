# utils/setting_loader.py
import yaml
import os

def load_settings(path="settings.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
