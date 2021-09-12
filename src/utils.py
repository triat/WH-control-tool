from typing import Any
from yaml import safe_load


def get_config(key: str, file_path="src/config.yaml") -> Any:
    with open(file_path, "r") as f:
        config = safe_load(f)
        return config.get(key)
