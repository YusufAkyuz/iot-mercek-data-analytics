import json
import pandas as pd
import re
from config_loader import load_config
from transformer import process_log
import argparse

def extract_log_data(raw_segments):
    try:
        # txt verisini okumak için parçalar birleştirilip, işaret düzenlemeleri yapılıyor.
        combined = ";".join(raw_segments)
        cleaned = combined.replace('""', '"').replace('"{', '{').replace('}"', '}')

        # logArrSize değeri
        size_match = re.search(r'"logArrSize"\s*:\s*{\s*"N"\s*:\s*"(\d+)"\s*}', cleaned)
        log_arr_size = int(size_match.group(1)) if size_match else 0

        # connState değeri
        conn_match = re.search(r'connState:\s*{\s*"S"\s*:\s*"(\w+)"\s*}', cleaned)
        conn_state = conn_match.group(1) if conn_match else "unknown"

        # logArr değerleri
        log_arr_matches = re.findall(r'"N"\s*:\s*"(\d+)"', cleaned)[1:]
        log_arr = [int(n) for n in log_arr_matches[:log_arr_size]]

        return log_arr, conn_state
    except Exception as e:
        print("Log parsing error:", e)
        return [], "error"

def main():
    parser = argparse.ArgumentParser(description="IoT Mercek Data Interpreter")
    parser.add_argument('--config', type=str, default='config/v1_10.json', help='Path to configuration file')
    parser.add_argument('--input', type=str, default='data/1.txt', help='Path to input data file')
    parser.add_argument('--output', type=str, default='output/processed_data.csv', help='Path to output CSV file')

    args = parser.parse_args()

    config = load_config(args.config)

    if config is None:
        print("The configuration file was not found.")
        return

    results = []

    with open(args.input, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(";")
            log_arr, conn_state = extract_log_data(parts)
            parsed = process_log(log_arr, config)
            parsed["connState"] = conn_state
            results.append(parsed)

    df = pd.DataFrame(results)
    df.to_csv(args.output, index=False)
    print(f"Data has been written to {args.output}")

if __name__ == "__main__":
    main()
