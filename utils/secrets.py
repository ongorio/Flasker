from pathlib import Path
import json

def get_secrets(file:str) -> dict:
    secrets_file = Path(file)
    secrets = json.loads(secrets_file.read_text())

    return secrets

