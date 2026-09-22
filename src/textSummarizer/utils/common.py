import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def get_yaml_config(config_path: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        config_path (Path): The path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty or cannot be parsed.
    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    """
    try:
        with open(config_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"The YAML file at {config_path} is empty.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Error parsing YAML file at {config_path}: {e}")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the YAML file at {config_path}: {e}")


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories specified in the list.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
