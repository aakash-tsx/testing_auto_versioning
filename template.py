import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

src = "src"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{src}/__init__.py",
    f"{src}/components/__init__.py",
    f"{src}/components/data_ingestion.py",
    f"{src}/components/data_validation.py",
    f"{src}/components/data_transformation.py",
    f"{src}/components/model_trainer.py",
    f"{src}/components/model_evaluation.py",
    f"{src}/utils/__init__.py",
    f"{src}/utils/common.py",
    f"{src}/config/__init__.py",
    f"{src}/config/config_manager.py",
    f"{src}/pipeline/__init__.py",
    f"{src}/entity/__init__.py",
    f"{src}/entity/config_entities.py",
    f"{src}/constants/__init__.py",
    f"{src}/exception/__init__.py",
    f"{src}/logger/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "research/trials.ipynb",
    "templates/index.html",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists!")
