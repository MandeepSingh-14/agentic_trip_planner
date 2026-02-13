import yaml 
import os

def load_config(config_path: str = "config/config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(f"Config loaded from {config_path}: {config}")
    return config