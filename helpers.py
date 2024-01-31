import hashlib
import pandas as pd
import json
from datetime import datetime


def save_to_json(json_data, path_to_json):
    """Сохраняет json в файл"""

    with open(path_to_json, 'w', encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False)


def save_json_to_xls(path_to_json, path_to_xls):
    """Сохраняет json в файл Excel"""

    pd.read_json(path_to_json).to_excel(path_to_xls)


def sha256sum(filename):
    """SHA256 File Checksum"""

    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def generate_external_id(head_id):
    """Генерирует external_id
    :param head_id: id с которого будет начинаться новый id
    """

    return f'{head_id}-{str(datetime.now().timestamp()).replace(".", "_")}'
