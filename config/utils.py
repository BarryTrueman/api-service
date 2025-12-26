# utils.py

import os
import json
import logging
from datetime import datetime
from typing import Dict, List
from pathlib import Path

class Config:
    def __init__(self, config_file: str):
        self.config_file = config_file

    def load_config(self) -> Dict:
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            logging.error(f"Could not find config file: {self.config_file}")
            return {}

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_logs_path() -> Path:
    return get_project_root() / 'logs'

def get_tmp_path() -> Path:
    return get_project_root() / 'tmp'

def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def get_timestamp() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')