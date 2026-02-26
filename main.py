import math

internal_k: float = .024
external_k: float = .048
b: float = 0.44
c: float = 0.725

eta: float = 377  # Intrinsic impedance of free space (Ohms)
rho_copper: float = 0.00067716  # Resistivity of copper in mils
alpha_copper: float = 0.00393   # Temperature coefficient of Copper

def calc_internal_trace_area_min(amps,input_temp_rise):
    area_min = (amps / (internal_k * (input_temp_rise ** b))) ** (1 / c)
    return round(area_min,4)

def calc_external_trace_area_min(amps,input_temp_rise):
    area_min = (amps / (external_k * (input_temp_rise ** b))) ** (1 / c)
    return round(area_min,4)

def calc_internal_trace_area_actual(trace_width_actual,thickness_mils):
    area_actual = trace_width_actual * thickness_mils
    return round(area_actual,4)

def calc_external_trace_area_actual(trace_width_actual,thickness_mils):
    area_actual = trace_width_actual * thickness_mils
    return round(area_actual,4)

def calc_min_trace_width_internal(area,thickness_mils):
    width = area/thickness_mils
    return round(width,4)

def calc_min_trace_width_external(area,thickness_mils):
    width = area/thickness_mils
    return round(width,4)

def calc_internal_trace_resistance(length,trace_area,temp_ambient):
    resistance = (rho_copper*(length/trace_area))*(1+(alpha_copper*(temp_ambient-25)))
    return round(resistance,4)

def calc_external_trace_resistance(length,trace_area,temp_ambient):
    resistance = (rho_copper*(length/trace_area))*(1+(alpha_copper*(temp_ambient-25)))
    return round(resistance,4)

def calc_internal_trace_voltage_drop(amps,resistance):
    voltage_drop = (amps*resistance)
    return round(voltage_drop,4)

def calc_external_trace_voltage_drop(amps,resistance):
    voltage_drop = (amps*resistance)
    return round(voltage_drop,4)

def convert_copper_weight(weight):
    converted_weight = weight * 1.378
    return converted_weight

def calc_total_thickness(base_weight,plating_weight):
    base_weight_converted = convert_copper_weight(base_weight)
    plating_weight_converted = convert_copper_weight(plating_weight)
    total_thickness = base_weight_converted + plating_weight_converted
    return total_thickness

def calc_single_microstrip_impedance(epsilon_r,height,thickness,width):
    Zo_microstrip = 87 / (math.sqrt(epsilon_r + 1.41)) * math.log((5.98 * height) / (0.8 * width) + thickness)
    return round(Zo_microstrip,4)

def calc_microstrip_diff_pair_impedance(epsilon_r,height,width,thickness,spacing):
    z_diff = 174 / (math.sqrt(epsilon_r + 1.41)) * (math.log((5.98 * height) / ((0.8 * width) + thickness))) * (1 - (0.48 * (math.exp(-0.96 * (spacing / height)))))
    return round(z_diff,4)

def calc_single_stripline_impedance(epsilon_r,height,thickness,width):
    Zo_stripline = (60 / math.sqrt(epsilon_r)) * math.log((1.9*(2 * height) + thickness) / ((0.8 * width) + thickness))
    return round(Zo_stripline,4)

def calc_stripline_diff_pair_impedance(Zo_stripline,width,height,thickness,spacing):
    z_diff = 2 * Zo_stripline * (1 - (0.347 * math.exp(-2.9 * ((spacing * height) + thickness) / (0.8 * width) + thickness)))
    return round(z_diff,4)