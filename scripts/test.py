import json
from config_loader import load_config
from transformer import process_log

config = load_config('./config/v1_10.json')

if config is None:
    print("Failed to load configuration.")
    exit(1)

logArr = [str(i % 256) for i in range(160)]
logArrSize = len(logArr)

meaningful = process_log(logArr[:logArrSize], config)
print(meaningful)

meaningful = process_log(logArr[:logArrSize], config)
print(meaningful)
