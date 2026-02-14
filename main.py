import math

internal_k: float = .024
external_k: float = .048
b: float = 0.44
c: float = 0.725

eta: int = 377  # Intrinsic impedance of free space
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

def calc_epsilon_effective(epsilon_relative,dielectric_height,trace_width):
    epsilon_effective = (((epsilon_relative+1)/2) + ((epsilon_relative-1)/2) * (1 + (12 * dielectric_height / trace_width) ** (-0.5)))
    return round(epsilon_effective,4)

def calc_width_effective(trace_width,trace_thickness,dielectric_height):
    width_effective = (trace_width + (trace_thickness/math.pi))*(1+math.log((2*dielectric_height)/trace_thickness))
    return round(width_effective,4)