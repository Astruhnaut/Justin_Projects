import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMainWindow, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from main import *

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCB DESIGN CALCULATOR")
        self.setGeometry(625, 100, 450, 800)

        # Set up layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        central_widget.setStyleSheet("background-color: white;")
        app.setStyleSheet("QWidget { color: black; }")

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setSpacing(8)

        self.amps_edit = QLineEdit()
        self.amps_edit.setFixedWidth(75)
        self.amps_edit.setStyleSheet("background-color: yellow;")

        self.length_edit = QLineEdit()
        self.length_edit.setFixedWidth(75)
        self.length_edit.setStyleSheet("background-color: yellow;")

        self.temp_rise_edit = QLineEdit()
        self.temp_rise_edit.setFixedWidth(75)
        self.temp_rise_edit.setStyleSheet("background-color: yellow;")

        self.copper_weight_edit = QLineEdit()
        self.copper_weight_edit.setFixedWidth(75)
        self.copper_weight_edit.setStyleSheet("background-color: yellow;")

        self.ambient_temp_edit = QLineEdit()
        self.ambient_temp_edit.setFixedWidth(75)
        self.ambient_temp_edit.setStyleSheet("background-color: yellow;")

        self.internal_trace_width_edit = QLineEdit()
        self.internal_trace_width_edit.setFixedWidth(75)
        self.internal_trace_width_edit.setStyleSheet("background-color: yellow;")

        self.external_trace_width_edit = QLineEdit()
        self.external_trace_width_edit.setFixedWidth(75)
        self.external_trace_width_edit.setStyleSheet("background-color: yellow;")

        self.min_area_result_internal = QLineEdit()
        self.min_area_result_internal.setReadOnly(True)
        self.min_area_result_internal.setFixedWidth(75)

        self.min_area_result_external = QLineEdit()
        self.min_area_result_external.setReadOnly(True)
        self.min_area_result_external.setFixedWidth(75)

        self.internal_actual_area_result = QLineEdit()
        self.internal_actual_area_result.setReadOnly(True)
        self.internal_actual_area_result.setFixedWidth(75)

        self.external_actual_area_result = QLineEdit()
        self.external_actual_area_result.setReadOnly(True)
        self.external_actual_area_result.setFixedWidth(75)

        self.internal_width_result = QLineEdit()
        self.internal_width_result.setReadOnly(True)
        self.internal_width_result.setFixedWidth(75)

        self.external_width_result = QLineEdit()
        self.external_width_result.setReadOnly(True)
        self.external_width_result.setFixedWidth(75)

        self.internal_resistance_result = QLineEdit()
        self.internal_resistance_result.setReadOnly(True)
        self.internal_resistance_result.setFixedWidth(75)

        self.internal_voltage_result = QLineEdit()
        self.internal_voltage_result.setReadOnly(True)
        self.internal_voltage_result.setFixedWidth(75)

        self.external_resistance_result = QLineEdit()
        self.external_resistance_result.setReadOnly(True)
        self.external_resistance_result.setFixedWidth(75)

        self.external_voltage_result = QLineEdit()
        self.external_voltage_result.setReadOnly(True)
        self.external_voltage_result.setFixedWidth(75)

        self.calculate = QPushButton("Calculate Results")
        self.calculate.setStyleSheet("background-color: lightblue;")
        self.calculate.clicked.connect(self.run_calc)

        form_layout.addRow("INPUTS:", QWidget())
        form_layout.addRow("Desired Trace Current in Amps", self.amps_edit)
        form_layout.addRow("Trace Length in mils", self.length_edit)
        form_layout.addRow("INTERNAL Trace Width in mils", self.internal_trace_width_edit)
        form_layout.addRow("EXTERNAL Trace Width in mils", self.external_trace_width_edit)
        form_layout.addRow("Temp Rise in Deg C", self.temp_rise_edit)
        form_layout.addRow("Ambient Temperature in Deg C", self.ambient_temp_edit)
        form_layout.addRow("Copper Weight in oz/ft^2", self.copper_weight_edit)


        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("RESULTS:", QWidget())

        form_layout.addRow("INTERNAL Minimum Trace Area in mils^2", self.min_area_result_internal)
        self.min_area_result_internal.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("EXTERNAL Minimum Trace Area in mils^2", self.min_area_result_external)
        self.min_area_result_external.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("INTERNAL Actual Trace Area in mils^2", self.internal_actual_area_result)
        self.internal_actual_area_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("EXTERNAL Actual Trace Area in mils^2", self.external_actual_area_result)
        self.external_actual_area_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("INTERNAL Minimum Trace Width in mils", self.internal_width_result)
        self.internal_width_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("EXTERNAL Minimum Trace Width in mils", self.external_width_result)
        self.external_width_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("INTERNAL Trace Resistance in Ohms", self.internal_resistance_result)
        self.internal_resistance_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("INTERNAL Trace Voltage Drop in Volts", self.internal_voltage_result)
        self.internal_voltage_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("EXTERNAL Trace Resistance in Ohms", self.external_resistance_result)
        self.external_resistance_result.setStyleSheet("background-color: lightgreen;")
        spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("EXTERNAL Trace Voltage Drop in Volts", self.external_voltage_result)
        self.external_voltage_result.setStyleSheet("background-color: lightgreen;")


        main_layout.addLayout(form_layout)

        main_layout.addWidget(self.calculate)

    def run_calc(self):

        # Calculate Minimum Internal Trace Area
        amps = float(self.amps_edit.text())
        temp_rise_C = float(self.temp_rise_edit.text())

        min_trace_area_internal = calc_internal_trace_area_min(amps,temp_rise_C)

        self.min_area_result_internal.setText(str(min_trace_area_internal))

        # Calculate Minimum External Trace Area
        min_trace_area_external = calc_external_trace_area_min(amps,temp_rise_C)

        self.min_area_result_external.setText(str(min_trace_area_external))

        # Calculate Internal Actual Trace Area
        weight = float(self.copper_weight_edit.text())
        converted_weight = weight * 1.378

        if self.internal_trace_width_edit.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.internal_trace_width_edit.text())

        internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width,converted_weight)

        self.internal_actual_area_result.setText(str(internal_actual_trace_area))

        # Calculate External Actual Trace Area
        if self.external_trace_width_edit.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.external_trace_width_edit.text())

        external_actual_trace_area = calc_external_trace_area_actual(actual_external_trace_width,converted_weight)

        self.external_actual_area_result.setText(str(external_actual_trace_area))

        # Calculate Minimum Internal Trace Width
        internal_trace_width = calc_min_trace_width_internal(min_trace_area_internal, converted_weight)

        self.internal_width_result.setText(str(internal_trace_width))

        # Calculate Minimum External Trace Width
        external_trace_width = calc_min_trace_width_external(min_trace_area_external, converted_weight)

        self.external_width_result.setText(str(external_trace_width))

        # Calculate Internal Trace Resistance
        length = float(self.length_edit.text())
        temp_ambient = float(self.ambient_temp_edit.text())

        internal_resistance = calc_internal_trace_resistance(length,internal_actual_trace_area,temp_ambient)

        self.internal_resistance_result.setText(str(internal_resistance))

        # Calculate External Trace Resistance
        external_resistance = calc_external_trace_resistance(length,external_actual_trace_area,temp_ambient)

        self.external_resistance_result.setText(str(external_resistance))

        # Calculate Internal Trace Voltage Drop
        voltage_drop_internal = calc_internal_trace_voltage_drop(amps,internal_resistance)

        self.internal_voltage_result.setText(str(voltage_drop_internal))

        # Calculate External Trace Voltage Drop
        voltage_drop_external = calc_external_trace_voltage_drop(amps,external_resistance)

        self.external_voltage_result.setText(str(voltage_drop_external))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(app.exec())

