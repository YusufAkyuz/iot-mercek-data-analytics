import json
import pandas as pd
import re
from config_loader import load_config
from transformer import process_log

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
    config = load_config('./config/v1_10.json')

    if config is None:
        print("The configuration file was not found.")
        return

    input_file = './data/1.txt'
    output_file = './output/processed_data.csv'

    all_results = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                parts = line.strip().split(";")
                if len(parts) < 5:
                    continue

                # ilk 4 parça appliance_id, lat, lon ve timestamp
                appliance_id = parts[0]
                lat = float(parts[1])
                lon = float(parts[2])
                try:
                    ts = int(parts[3])
                except Exception as e:
                    print(f"Timestamp conversion error: {parts[3]} is not a valid timestamp.")
    
                # Geri kalan parçalar log verisi bunları düzenlemek ve işlemek için extract_log_data fonksiyonu çağrılıyor.
                log_arr, conn_state = extract_log_data(parts[4:])

                result = process_log(log_arr, config)
                result.update({
                    "ApplianceId": appliance_id,
                    "Latitude": lat,
                    "Longitude": lon,
                    "Timestamp": ts,
                    "ConnState": conn_state
                })
                all_results.append(result)
            except Exception as e:
                print(f"The row could not be processed: {e}")
                continue

    # Olusan çıktıları csv de kaydetme
    df = pd.DataFrame(all_results)
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"{len(all_results)} record was successfully processed and saved to file '{output_file}'.")

if __name__ == "__main__":
    main()
