import pandas as pd
from mappers import *

mapper_funcs = {
    "getBitwiseEnum": get_bitwise_enum,
    "getValue": get_value,
    "calcVoltage": calc_voltage,
    "calcSpin": calc_spin,
    "getEnum": get_enum,
    "getEnumOrDefault": get_enum_or_default,
    "calcChildLock": calc_child_lock,
    "getAsMin": get_as_min,
    "calcHighLow": calc_high_low,
    "calcHeatTime": calc_heat_time,
}


def process_log(log_arr, config):
    result = {}
    for key, meta in config.items():
        info = meta["modelInfo"]
        indexes = info["index"]
        mapper = meta["mapperFunc"]
        source_type = meta["sourceType"]
        values = [log_arr[i] for i in indexes]
        func = mapper_funcs.get(mapper)
        if func:
            result[key] = func(values if len(values) > 1 else values[0], info.get("bitSetEnumValues", info.get("enumValues", {})))
    return result
