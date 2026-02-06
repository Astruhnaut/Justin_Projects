import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMainWindow, QSpacerItem, QSizePolicy, QTabWidget
from PyQt6.QtCore import Qt
from main import *

class TabWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCB DESIGN CALCULATOR")
        self.setGeometry(625, 100, 450, 550)

        # Set up layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # self.central_widget.setStyleSheet("background-color: white;")

        # Create the QTabWidget
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        self.trace_width_tab = QWidget()
        self.tabs.addTab(self.trace_width_tab,"Trace Width")
        self.init_trace_width_tab_ui()

        # Create the trace resistance tab
        self.trace_resistance_tab = QWidget()
        self.tabs.addTab(self.trace_resistance_tab, "Voltage Drop/Resistance")
        self.init_drop_resistance_tab_ui()

    def init_trace_width_tab_ui(self):

        trace_width_tab_layout = QVBoxLayout()

        self.trace_width_tab.setLayout(trace_width_tab_layout)

        #*******INPUTS*******

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_width_tab_layout.addWidget(label_inputs)

        amps_hbox = QHBoxLayout()
        amps_label = QLabel("Desired Trace Current in Amps")
        self.amps_edit = QLineEdit()
        self.amps_edit.setFixedWidth(75)

        amps_hbox.addWidget(amps_label)
        amps_hbox.addWidget(self.amps_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(amps_hbox)

        internal_width_hbox = QHBoxLayout()
        internal_width_label = QLabel("INTERNAL Trace Width in mils")
        self.internal_width_edit = QLineEdit()
        self.internal_width_edit.setFixedWidth(75)

        internal_width_hbox.addWidget(internal_width_label)
        internal_width_hbox.addWidget(self.internal_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_width_hbox)

        external_width_hbox = QHBoxLayout()
        external_width_label = QLabel("EXTERNAL Trace Width in mils")
        self.external_width_edit = QLineEdit()
        self.external_width_edit.setFixedWidth(75)

        external_width_hbox.addWidget(external_width_label)
        external_width_hbox.addWidget(self.external_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_width_hbox)

        temp_rise_hbox = QHBoxLayout()
        temp_rise_label = QLabel("Temperature Rise in Celsius")
        self.temp_rise_edit = QLineEdit()
        self.temp_rise_edit.setFixedWidth(75)

        temp_rise_hbox.addWidget(temp_rise_label)
        temp_rise_hbox.addWidget(self.temp_rise_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(temp_rise_hbox)

        copper_weight_hbox = QHBoxLayout()
        copper_weight_label = QLabel("Copper Weight in oz/ft^2")
        self.copper_weight_edit = QLineEdit()
        self.copper_weight_edit.setFixedWidth(75)

        copper_weight_hbox.addWidget(copper_weight_label)
        copper_weight_hbox.addWidget(self.copper_weight_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(copper_weight_hbox)


        #*******RESULTS*******


        # Create a spacer between INPUTS and RESULTS
        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        trace_width_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_width_tab_layout.addWidget(label_results)

        internal_trace_width_hbox = QHBoxLayout()
        internal_trace_width_label = QLabel("INTERNAL Minimum Trace Width in mils")
        self.min_trace_width_internal_result = QLineEdit()
        self.min_trace_width_internal_result.setReadOnly(True)
        self.min_trace_width_internal_result.setFixedWidth(75)

        internal_trace_width_hbox.addWidget(internal_trace_width_label)
        internal_trace_width_hbox.addWidget(self.min_trace_width_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_trace_width_hbox)

        internal_min_area_hbox = QHBoxLayout()
        internal_min_area_label = QLabel("INTERNAL Minimum Trace Area in mils^2")
        self.min_trace_area_internal_result = QLineEdit()
        self.min_trace_area_internal_result.setReadOnly(True)
        self.min_trace_area_internal_result.setFixedWidth(75)

        internal_min_area_hbox.addWidget(internal_min_area_label)
        internal_min_area_hbox.addWidget(self.min_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_min_area_hbox)

        internal_actual_area_hbox = QHBoxLayout()
        internal_actual_area_label = QLabel("INTERNAL Actual Trace Area in mils^2")
        self.actual_trace_area_internal_result = QLineEdit()
        self.actual_trace_area_internal_result.setReadOnly(True)
        self.actual_trace_area_internal_result.setFixedWidth(75)

        internal_actual_area_hbox.addWidget(internal_actual_area_label)
        internal_actual_area_hbox.addWidget(self.actual_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_actual_area_hbox)

        external_trace_width_hbox = QHBoxLayout()
        external_trace_width_label = QLabel("EXTERNAL Minimum Trace Width in mils")
        self.min_trace_width_external_result = QLineEdit()
        self.min_trace_width_external_result.setReadOnly(True)
        self.min_trace_width_external_result.setFixedWidth(75)

        external_trace_width_hbox.addWidget(external_trace_width_label)
        external_trace_width_hbox.addWidget(self.min_trace_width_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_trace_width_hbox)

        external_min_area_hbox = QHBoxLayout()
        external_min_area_label = QLabel("EXTERNAL Minimum Trace Area in mils^2")
        self.min_trace_area_external_result = QLineEdit()
        self.min_trace_area_external_result.setReadOnly(True)
        self.min_trace_area_external_result.setFixedWidth(75)

        external_min_area_hbox.addWidget(external_min_area_label)
        external_min_area_hbox.addWidget(self.min_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_min_area_hbox)

        external_actual_area_hbox = QHBoxLayout()
        external_actual_area_label = QLabel("EXTERNAL Actual Trace Area in mils^2")
        self.actual_trace_area_external_result = QLineEdit()
        self.actual_trace_area_external_result.setReadOnly(True)
        self.actual_trace_area_external_result.setFixedWidth(75)

        external_actual_area_hbox.addWidget(external_actual_area_label)
        external_actual_area_hbox.addWidget(self.actual_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_actual_area_hbox)

        calculate = QPushButton("Calculate Results")
        calculate.setStyleSheet("background-color: lightblue;")
        calculate.clicked.connect(self.run_width_calc)
        trace_width_tab_layout.addWidget(calculate)

        # Set the layout for the main window
        self.setLayout(trace_width_tab_layout)

        trace_width_tab_layout.addStretch()


    def init_drop_resistance_tab_ui(self):

        trace_resistance_tab_layout = QVBoxLayout()
        self.trace_resistance_tab.setLayout(trace_resistance_tab_layout)


        # *******INPUTS*******

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_resistance_tab_layout.addWidget(label_inputs)

        length_hbox = QHBoxLayout()
        length_label = QLabel("Actual Trace Length in mils")
        self.length_edit = QLineEdit()
        self.length_edit.setFixedWidth(75)

        length_hbox.addWidget(length_label)
        length_hbox.addWidget(self.length_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(length_hbox)


        #*******RESULTS*******


        trace_resistance_hbox = QHBoxLayout()
        internal_resistance_label = QLabel("INTERNAL Trace Resistance")
        self.internal_resistance_result = QLineEdit()
        self.internal_resistance_result.setReadOnly(True)
        self.internal_resistance_result.setFixedWidth(75)

        trace_resistance_hbox.addWidget(internal_resistance_label)
        trace_resistance_hbox.addWidget(self.internal_resistance_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_resistance_hbox)

        trace_voltage_drop_hbox = QHBoxLayout()
        internal_drop_label = QLabel("INTERNAL Trace Voltage Drop")
        self.internal_resistance_result = QLineEdit()
        self.internal_resistance_result.setReadOnly(True)
        self.internal_resistance_result.setFixedWidth(75)

        trace_resistance_hbox.addWidget(internal_drop_label)
        trace_resistance_hbox.addWidget(self.internal_resistance_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_voltage_drop_hbox)

        calculate = QPushButton("Calculate Results")
        calculate.setStyleSheet("background-color: lightblue;")
        calculate.clicked.connect(self.run_resistance_calc)
        trace_resistance_tab_layout.addWidget(calculate)

        # Set the layout for the main window
        self.setLayout(trace_resistance_tab_layout)

        trace_resistance_tab_layout.addStretch()

    def run_width_calc(self):

        # Calculate Minimum Internal Trace Area
        self.amps = float(self.amps_edit.text())
        temp_rise_C = float(self.temp_rise_edit.text())

        min_trace_area_internal = calc_internal_trace_area_min(self.amps, temp_rise_C)

        self.min_trace_area_internal_result.setText(str(self.min_trace_area_internal_result))

        # Calculate Minimum External Trace Area
        min_trace_area_external = calc_external_trace_area_min(self.amps, temp_rise_C)

        self.min_trace_area_external_result.setText(str(min_trace_area_external))

        # Calculate Internal Actual Trace Area
        weight = float(self.copper_weight_edit.text())
        converted_weight = weight * 1.378

        if self.internal_width_edit.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.internal_width_edit.text())

        self.internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width, converted_weight)

        self.actual_trace_area_internal_result.setText(str(self.internal_actual_trace_area))

        # Calculate External Actual Trace Area
        if self.external_width_edit.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.external_width_edit.text())

        self.external_actual_trace_area = calc_external_trace_area_actual(actual_external_trace_width, converted_weight)

        self.actual_trace_area_external_result.setText(str(self.external_actual_trace_area))

        # Calculate Minimum Internal Trace Width
        internal_trace_width = calc_min_trace_width_internal(min_trace_area_internal, converted_weight)

        self.min_trace_width_internal_result.setText(str(internal_trace_width))

        # Calculate Minimum External Trace Width
        external_trace_width = calc_min_trace_width_external(min_trace_area_external, converted_weight)

        self.min_trace_width_external_result.setText(str(external_trace_width))

    def run_resistance_calc(self):

        # Calculate Internal Trace Resistance
        length = float(self.length_edit.text())
        temp_ambient = float(self.ambient_temp_edit.text())

        internal_resistance = calc_internal_trace_resistance(length,self.internal_actual_trace_area,temp_ambient)

        self.internal_resistance_result.setText(str(internal_resistance))

        # Calculate External Trace Resistance
        external_resistance = calc_external_trace_resistance(length,self.external_actual_trace_area,temp_ambient)

        self.external_resistance_result.setText(str(external_resistance))

        # Calculate Internal Trace Voltage Drop
        voltage_drop_internal = calc_internal_trace_voltage_drop(self.amps,internal_resistance)

        self.internal_voltage_result.setText(str(voltage_drop_internal))

        # Calculate External Trace Voltage Drop
        voltage_drop_external = calc_external_trace_voltage_drop(self.amps,external_resistance)

        self.external_voltage_result.setText(str(voltage_drop_external))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidgetApp()
    window.show()
    sys.exit(app.exec())

