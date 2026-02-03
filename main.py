internal_trace_resistance = float

external_trace_resistance = float

internal_voltage_drop = float

external_voltage_drop = float

internal_min_trace_width = float
actual_trace_width_internal = float

external_min_trace_width = float
actual_trace_width_external = float

internal_area_min = float
internal_area_actual = float

external_area_min = float
external_area_actual = float

internal_k: float = .024
external_k: float = .048
b: float = 0.44
c: float = 0.725

rho_copper: float = 0.00067716  #Resistivity of copper in mils
alpha_copper: float = 0.00393   #Temperature coefficient of Copper

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
