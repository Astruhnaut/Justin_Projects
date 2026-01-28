internal_trace_resistance = float

internal_voltage_drop = float

min_trace_width_internal = float
actual_trace_width_internal = float

min_trace_width_external = float
actual_trace_width_external = float

internal_area_min = float
internal_area_actual = float

internal_k: float = .024
internal_b: float = 0.44
internal_c: float = 0.725

external_k: float = 0.048
external_b: float = 0.44
external_c: float = 0.725

rho_copper: float = 0.00067716  #Resistivity of copper in mils
alpha_copper: float = 0.00393   #Temperature coefficient of Copper

calc_type = string

temp_rise = float(input("Enter the temperature rise in Deg C: "))

def calc_trace_area_min(amps, k, input_temp_rise, b, c):
    area_min = (amps / (k * (input_temp_rise ** b))) ** (1 / c)
    return area_min

internal_area_min = calc_trace_area_min(current, internal_k, temp_rise, internal_b, internal_c)

def calc_trace_area_actual(trace_width_actual,thickness_mils):
    area_actual = trace_width_actual * thickness_mils
    return area_actual

def calc_min_trace_width_internal(area,thickness_mils):
    width = area/thickness_mils
    return width

min_trace_width_internal = calc_min_trace_width_internal(internal_area_min, copper_thickness_mils)

def calc_internal_trace_resistance(resistivity,length,trace_area,alpha,temp_ambient):
    resistance = (resistivity*(length/trace_area))*(1+(alpha*(temp_ambient-25)))
    return resistance

def calc_internal_trace_voltage_drop(amps,resistance):
    voltage_drop = (amps*resistance)
    return voltage_drop


if calc_type == "v":

    trace_width = float(input("Enter the trace width in mils: "))
    copper_thickness = float(input("Enter the copper thickness in oz/ft^2: "))
    trace_length = float(input("Enter the length of the trace in mils: "))
    ambient_temp = float(input("Enter the ambient temperature in Deg C: "))
    current = float(input("Enter the desired trace current in Amps: "))

    copper_thickness_mils: float = copper_thickness * 1.378  # Convert copper thickness from oz/ft^2 to mils

    internal_area_actual = calc_trace_area_actual(trace_width, copper_thickness_mils)
    internal_trace_resistance = calc_internal_trace_resistance(rho_copper, trace_length, internal_area_actual,alpha_copper, ambient_temp)
    internal_voltage_drop = calc_internal_trace_voltage_drop(current, internal_trace_resistance)
