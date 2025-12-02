# observability/logger.py
import logging
import logging.config
import yaml
from pathlib import Path


def setup_logging(config_path: str = "config/logging.yaml"):
    with open(Path(config_path), "r") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)


logger = logging.getLogger("app")
