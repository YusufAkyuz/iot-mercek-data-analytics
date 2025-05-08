def get_bitwise_enum(value, enum_map):
    bin_val = format(int(value), '08b')[::-1]
    return [enum_map[str(i)] for i, bit in enumerate(bin_val) 
            if bit == '1' and str(i) in enum_map and enum_map[str(i)]]

def get_enum(value, enum_map):
    return enum_map.get(str(value), "Unknown")

def get_enum_or_default(value, enum_map):
    return enum_map.get(str(value), "None")

def get_value(value, _):
    return value

def calc_voltage(value, _):
    return int(value) * 10

def calc_spin(value, _):
    return int(value) * 10

def get_as_min(values, _):
    return int(values[0]) * 60 + int(values[1])

def calc_high_low(values, _):
    return (int(values[0]) << 8) + int(values[1])

def calc_heat_time(value, _):
    return int(value)

def calc_child_lock(value, _): 
    return value == "1"
