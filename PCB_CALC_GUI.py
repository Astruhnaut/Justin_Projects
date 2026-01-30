import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMainWindow, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from main import *

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCB DESIGN CALCULATOR")
        self.resize(800, 600)

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

        self.trace_width_edit = QLineEdit()
        self.trace_width_edit.setFixedWidth(75)
        self.trace_width_edit.setStyleSheet("background-color: yellow;")

        self.min_area_result = QLineEdit()
        self.min_area_result.setReadOnly(True)
        self.min_area_result.setFixedWidth(75)

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
        self.calculate.setStyleSheet("background-color: red;")
        self.calculate.clicked.connect(self.run_calc)

        form_layout.addRow("INPUTS:", QWidget())
        form_layout.addRow("Desired Trace Current in Amps", self.amps_edit)
        form_layout.addRow("Trace Length in mils", self.length_edit)
        form_layout.addRow("Temp Rise in Deg C", self.temp_rise_edit)
        form_layout.addRow("Copper Weight in oz/ft^2", self.copper_weight_edit)
        form_layout.addRow("Ambient Temperature in Deg C", self.ambient_temp_edit)
        form_layout.addRow("Trace Width in mils", self.trace_width_edit)

        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        form_layout.addItem(spacer)

        form_layout.addRow("RESULTS:", QWidget())

        form_layout.addRow("Minimum Trace Area in mils^2", self.min_area_result)
        self.min_area_result.setStyleSheet("background-color: lightgreen;")

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

        amps = float(self.amps_edit.text())
        temp_rise_C = float(self.temp_rise_edit.text())

        min_trace_area = calc_trace_area_min(amps,temp_rise_C)

        self.min_area_result.setText(str(min_trace_area))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(app.exec())

