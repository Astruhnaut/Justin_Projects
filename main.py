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


if __name__ == "__main__":

    calc_type = input("Is this an Internal or External Trace? [i/e]")

    calc_mode = input("Are we solving for Voltage Drop or Minimum Trace Width? [v/w]")

    if calc_type == "i" and calc_mode == "v":

        current = float(input("Enter the desired trace current in Amps: "))
        trace_width = float(input("Enter the trace width in mils: "))
        copper_thickness = float(input("Enter the copper thickness in oz/ft^2: "))
        trace_length = float(input("Enter the trace length in mils: "))
        ambient_temp = float(input("Enter the ambient temperature in Deg C: "))

        copper_thickness_mils: float = copper_thickness * 1.378  # Convert copper thickness from oz/ft^2 to mils

        internal_area_actual = calc_internal_trace_area_actual(trace_width, copper_thickness_mils)
        internal_trace_resistance = calc_internal_trace_resistance(trace_length,internal_area_actual,ambient_temp)
        internal_voltage_drop = calc_internal_trace_voltage_drop(current, internal_trace_resistance)

        print(f"Voltage Drop is: {internal_voltage_drop:.4f} Volts")

    elif calc_type == "i" and calc_mode == "w":

        current = float(input("Enter the desired trace current in Amps: "))
        copper_thickness = float(input("Enter the copper thickness in oz/ft^2: "))
        temp_rise = float(input("Enter the temperature rise in Deg C: "))

        copper_thickness_mils: float = copper_thickness * 1.378  # Convert copper thickness from oz/ft^2 to mils

        internal_area_min = calc_internal_trace_area_min(current,temp_rise)
        internal_min_trace_width = calc_min_trace_width_internal(internal_area_min, copper_thickness_mils)

        print(f"Minimum Internal Trace Width is: {internal_min_trace_width:.4f} mils")

    if calc_type == "e" and calc_mode == "v":

        current = float(input("Enter the desired trace current in Amps: "))
        trace_width = float(input("Enter the trace width in mils: "))
        copper_thickness = float(input("Enter the copper thickness in oz/ft^2: "))
        trace_length = float(input("Enter the trace length in mils: "))
        ambient_temp = float(input("Enter the ambient temperature in Deg C: "))

        copper_thickness_mils: float = copper_thickness * 1.378  # Convert copper thickness from oz/ft^2 to mils

        external_area_actual = calc_external_trace_area_actual(trace_width, copper_thickness_mils)
        external_trace_resistance = calc_external_trace_resistance(trace_length,external_area_actual,ambient_temp)
        external_voltage_drop = calc_external_trace_voltage_drop(current, external_trace_resistance)

        print(f"Voltage Drop is: {external_voltage_drop:.4f} Volts")

    elif calc_type == "e" and calc_mode == "w":

        current = float(input("Enter the desired trace current in Amps: "))
        copper_thickness = float(input("Enter the copper thickness in oz/ft^2: "))
        temp_rise = float(input("Enter the temperature rise in Deg C: "))

        copper_thickness_mils: float = copper_thickness * 1.378  # Convert copper thickness from oz/ft^2 to mils

        external_area_min = calc_external_trace_area_min(current,temp_rise)
        external_min_trace_width = calc_min_trace_width_external(external_area_min, copper_thickness_mils)

        print(f"Minimum External Trace Width is: {external_min_trace_width:.4f} mils")
