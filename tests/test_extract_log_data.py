from scripts.test import extract_log_data

def test_extract_log_data_success():
    raw_segments = [
        '"logArrSize": {"N": "2"}',
        'connState: {"S": "online"}',
        '{"N":"8"}', '{"N":"12"}', '{"N":"5"}'
    ]
    log_arr, conn_state = extract_log_data(raw_segments)
    assert log_arr == [8, 12]
    assert conn_state == "online"

def test_extract_log_data_invalid_size():
    raw_segments = ['"logArrSize": {"N": "invalid"}']  # Non-integer size
    log_arr, conn_state = extract_log_data(raw_segments)
    assert log_arr == []
    assert conn_state == "unknown"