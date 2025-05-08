import json
import os

# İlk olarak varolan config.json dosyasını kontrol edip python objesi haline çevirme işlemi gerçekleştirilecek.
def load_config(config_path):
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            try:
                config = json.load(file)
                return config
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
                return None
    else:
        print("File path not found:", config_path)
        return None
