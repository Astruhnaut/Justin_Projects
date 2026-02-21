import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QFormLayout, QMainWindow, QSpacerItem, QSizePolicy, QTabWidget, QCheckBox
from PyQt6.QtCore import Qt
from main import *
from LabeledEdit import *

class TabWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCB DESIGN CALCULATOR")
        self.setGeometry(625, 100, 450, 625)

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

        self.diff_pair_impedance_tab = QWidget()
        self.tabs.addTab(self.diff_pair_impedance_tab, "Microstrip Diff Pair")
        self.init_diff_pair_tab_ui()

    def init_diff_pair_tab_ui(self):

        diff_pair_tab_layout = QVBoxLayout()

        self.diff_pair_impedance_tab.setLayout(diff_pair_tab_layout)

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        diff_pair_tab_layout.addWidget(label_inputs)

        # *******INPUTS*******

        # Relative Permittivity Input
        self.epsilon_r_widget = LabeledLineEdit("Relative Permittivity")
        diff_pair_tab_layout.addWidget(self.epsilon_r_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.epsilon_r_widget.layout)

        # Dielectric Height Input
        self.dielectric_height_widget = LabeledLineEdit("Dielectric Height (mils)")
        diff_pair_tab_layout.addWidget(self.dielectric_height_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.dielectric_height_widget.layout)

        # Base Copper Weight Input
        self.base_weight_widget = LabeledLineEdit("Base Copper Weight (oz/ft^2)")
        diff_pair_tab_layout.addWidget(self.base_weight_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.base_weight_widget.layout)

        # Plating Weight Input
        self.plating_weight_widget = LabeledLineEdit("Plating Copper Weight (oz/ft^2)")
        diff_pair_tab_layout.addWidget(self.plating_weight_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.plating_weight_widget.layout)

        # Trace Width Input
        self.trace_width_widget = LabeledLineEdit("Trace Width (mils)")
        diff_pair_tab_layout.addWidget(self.trace_width_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.trace_width_widget.layout)

        # Trace Spacing Input
        self.trace_spacing_widget = LabeledLineEdit("Trace Spacing (mils)")
        diff_pair_tab_layout.addWidget(self.trace_spacing_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.trace_spacing_widget.layout)


        # *******RESULTS*******

        # Create a spacer between INPUTS and RESULTS
        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        diff_pair_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        diff_pair_tab_layout.addWidget(label_results)

        # Effective Permittivity Result
        self.epsilon_eff_result_widget = LabeledLineEdit("Effective Permittivity")
        diff_pair_tab_layout.addWidget(self.epsilon_eff_result_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.epsilon_eff_result_widget.layout)

        # Effective Trace Width Result
        self.width_eff_result_widget = LabeledLineEdit("Effective Trace Width (mils)")
        diff_pair_tab_layout.addWidget(self.width_eff_result_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.width_eff_result_widget.layout)

        # Single Trace Impedance Result
        self.single_trace_impedance_result_widget = LabeledLineEdit("Single Trace Impedance (Ohms)")
        diff_pair_tab_layout.addWidget(self.single_trace_impedance_result_widget)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(self.single_trace_impedance_result_widget.layout)



        diff_pair_tab_layout.addStretch()

        calculate = QPushButton("Calculate Results")
        calculate.setStyleSheet("background-color: green;")
        calculate.clicked.connect(self.run_impedance_calc)
        diff_pair_tab_layout.addWidget(calculate)

        # Set the layout for the main window
        self.setLayout(diff_pair_tab_layout)

    def init_trace_width_tab_ui(self):

        trace_width_tab_layout = QVBoxLayout()

        self.trace_width_tab.setLayout(trace_width_tab_layout)

        self.internal_calc_checkbox = QCheckBox('focus INTERNAL')
        self.internal_calc_checkbox.setChecked(False) # Initially NOT checked

        self.internal_calc_checkbox.toggled.connect(self.toggle_external_width)

        trace_width_tab_layout.addWidget(self.internal_calc_checkbox)

        self.external_calc_checkbox = QCheckBox('focus EXTERNAL')
        self.external_calc_checkbox.setChecked(False) # Initially NOT checked

        self.external_calc_checkbox.toggled.connect(self.toggle_internal_width)

        trace_width_tab_layout.addWidget(self.external_calc_checkbox)

        #*******INPUTS*******

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_width_tab_layout.addWidget(label_inputs)

        # Amps Input
        self.amps_edit_widget = LabeledLineEdit("Desired Current (Amps)")
        trace_width_tab_layout.addWidget(self.amps_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.amps_edit_widget.layout)

        # Internal Trace Width Input
        self.internal_trace_width_edit_widget = LabeledLineEdit("INTERNAL Trace Width (mils)")
        trace_width_tab_layout.addWidget(self.internal_trace_width_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.internal_trace_width_edit_widget.layout)

        # External Trace Width Input
        self.external_trace_width_edit_widget = LabeledLineEdit("EXTERNAL Trace Width (mils)")
        trace_width_tab_layout.addWidget(self.external_trace_width_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.external_trace_width_edit_widget.layout)

        # Temperature Rise Input
        self.temp_rise_edit_widget = LabeledLineEdit("Temp Rise (Celsius)")
        trace_width_tab_layout.addWidget(self.temp_rise_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.temp_rise_edit_widget.layout)
        
        # Copper Weight Input
        self.copper_weight_edit_widget = LabeledLineEdit("Copper Weight (oz/ft^2)")
        trace_width_tab_layout.addWidget(self.copper_weight_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.copper_weight_edit_widget.layout)



        #*******RESULTS*******


        # Create a spacer between INPUTS and RESULTS
        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        trace_width_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_width_tab_layout.addWidget(label_results)


        # Internal Minimum Trace Width Result
        self.internal_trace_width_widget = LabeledLineEdit("INTERNAL Minimum Trace Width (mils)")
        trace_width_tab_layout.addWidget(self.internal_trace_width_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.internal_trace_width_widget.layout)


        # Internal Minimum Trace Area Result
        self.internal_trace_area_widget = LabeledLineEdit("INTERNAL Minimum Trace Area (mils^2)")
        trace_width_tab_layout.addWidget(self.internal_trace_area_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.internal_trace_area_widget.layout)


        # Internal Actual Trace Area Result
        self.internal_actual_trace_area_widget = LabeledLineEdit("INTERNAL Actual Trace Area (mils^2)")
        trace_width_tab_layout.addWidget(self.internal_actual_trace_area_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.internal_actual_trace_area_widget.layout)


        # External Minimum Trace Width Result
        self.external_trace_width_widget = LabeledLineEdit("EXTERNAL Minimum Trace Width (mils)")
        trace_width_tab_layout.addWidget(self.external_trace_width_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.external_trace_width_widget.layout)


        # External Minimum Trace Area Result
        self.external_trace_area_widget = LabeledLineEdit("EXTERNAL Minimum Trace Area (mils^2)")
        trace_width_tab_layout.addWidget(self.external_trace_area_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.external_trace_area_widget.layout)


        # External Actual Trace Area Result
        self.external_actual_trace_area_widget = LabeledLineEdit("EXTERNAL Actual Trace Area (mils^2)")
        trace_width_tab_layout.addWidget(self.external_actual_trace_area_widget)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(self.external_actual_trace_area_widget.layout)

        trace_width_tab_layout.addStretch()

        calculate = QPushButton("Calculate Results")
        calculate.setStyleSheet("background-color: green;")
        calculate.clicked.connect(self.run_calc)
        trace_width_tab_layout.addWidget(calculate)

        # Set the layout for the main window
        self.setLayout(trace_width_tab_layout)


    def init_drop_resistance_tab_ui(self):

        trace_resistance_tab_layout = QVBoxLayout()
        self.trace_resistance_tab.setLayout(trace_resistance_tab_layout)

        self.internal_calc_checkbox2 = QCheckBox('focus INTERNAL')
        self.internal_calc_checkbox2.setChecked(False) # Initially NOT checked

        self.internal_calc_checkbox2.toggled.connect(self.toggle_external_vd_ohms)

        trace_resistance_tab_layout.addWidget(self.internal_calc_checkbox2)

        self.external_calc_checkbox2 = QCheckBox('focus EXTERNAL')
        self.external_calc_checkbox2.setChecked(False) # Initially NOT checked

        self.external_calc_checkbox2.toggled.connect(self.toggle_internal_vd_ohms)

        trace_resistance_tab_layout.addWidget(self.external_calc_checkbox2)


        # *******INPUTS*******


        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_resistance_tab_layout.addWidget(label_inputs)


        # Desired Current Input
        self.vd_amps_edit_widget = LabeledLineEdit("Desired Current (Amps)")
        trace_resistance_tab_layout.addWidget(self.vd_amps_edit_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.vd_amps_edit_widget.layout)


        # Internal Trace Width Input
        self.vd_internal_width_widget = LabeledLineEdit("INTERNAL Trace Width (mils)")
        trace_resistance_tab_layout.addWidget(self.vd_internal_width_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.vd_internal_width_widget.layout)


        # External Trace Width Input
        self.vd_external_width_widget = LabeledLineEdit("EXTERNAL Trace Width (mils)")
        trace_resistance_tab_layout.addWidget(self.vd_external_width_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.vd_external_width_widget.layout)


        # Actual Trace Length Input
        self.trace_length_widget = LabeledLineEdit("Actual Trace Length (mils)")
        trace_resistance_tab_layout.addWidget(self.trace_length_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.trace_length_widget.layout)


        # Ambient Temperature Input
        self.ambient_temp_widget = LabeledLineEdit("Ambient Temp (Celsius)")
        trace_resistance_tab_layout.addWidget(self.ambient_temp_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.ambient_temp_widget.layout)


        # Copper Weight Input
        self.vd_copper_weight_widget = LabeledLineEdit("Copper Weight (oz/ft^2)")
        trace_resistance_tab_layout.addWidget(self.vd_copper_weight_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.vd_copper_weight_widget.layout)


        #*******RESULTS*******


        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        trace_resistance_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_resistance_tab_layout.addWidget(label_results)


        # Internal Trace Resistance Result
        self.internal_resistance_widget = LabeledLineEdit("INTERNAL Trace Resistance (Ohms)")
        trace_resistance_tab_layout.addWidget(self.internal_resistance_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.internal_resistance_widget.layout)


        # Internal Trace Voltage Drop Result
        self.internal_drop_widget = LabeledLineEdit("INTERNAL Trace Voltage Drop (Volts)")
        trace_resistance_tab_layout.addWidget(self.internal_drop_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.internal_drop_widget.layout)


        # External Trace Resistance Result
        self.external_resistance_widget = LabeledLineEdit("EXTERNAL Trace Resistance (Ohms)")
        trace_resistance_tab_layout.addWidget(self.external_resistance_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.external_resistance_widget.layout)


        # External Trace Voltage Drop Result
        self.external_drop_widget = LabeledLineEdit("EXTERNAL Trace Voltage Drop (Volts)")
        trace_resistance_tab_layout.addWidget(self.external_drop_widget)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(self.external_drop_widget.layout)

        trace_resistance_tab_layout.addStretch()

        calculate = QPushButton("Calculate Results")
        calculate.setStyleSheet("background-color: green;")
        calculate.clicked.connect(self.run_vd_resistance_calc)
        trace_resistance_tab_layout.addWidget(calculate)

        # Set the layout for the main window
        self.setLayout(trace_resistance_tab_layout)

    def run_calc(self):

        # Calculate Minimum Internal Trace Area
        amps = float(self.amps_edit_widget.text())
        temp_rise_C = float(self.temp_rise_edit_widget.text())

        min_trace_area_internal = calc_internal_trace_area_min(amps, temp_rise_C)

        self.internal_trace_area_widget.setText(str(min_trace_area_internal))

        # Calculate Minimum External Trace Area
        min_trace_area_external = calc_external_trace_area_min(amps, temp_rise_C)

        self.external_trace_area_widget.setText(str(min_trace_area_external))

        # Calculate Internal Actual Trace Area
        weight = float(self.copper_weight_edit_widget.text())
        converted_weight = convert_copper_weight(weight)

        if self.internal_trace_width_edit_widget.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.internal_trace_width_edit_widget.text())

        internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width, converted_weight)

        self.internal_actual_trace_area_widget.setText(str(internal_actual_trace_area))

        # Calculate External Actual Trace Area
        if self.external_trace_width_edit_widget.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.external_trace_width_edit_widget.text())

        external_actual_trace_area = calc_external_trace_area_actual(actual_external_trace_width, converted_weight)

        self.external_actual_trace_area_widget.setText(str(external_actual_trace_area))

        # Calculate Minimum Internal Trace Width
        internal_trace_width = calc_min_trace_width_internal(min_trace_area_internal, converted_weight)

        self.internal_trace_width_widget.setText(str(internal_trace_width))

        # Calculate Minimum External Trace Width
        external_trace_width = calc_min_trace_width_external(min_trace_area_external, converted_weight)

        self.external_trace_width_widget.setText(str(external_trace_width))

    def run_vd_resistance_calc(self):

        amps = float(self.vd_amps_edit_widget.text())
        length = float(self.trace_length_widget.text())
        temp_ambient = float(self.ambient_temp_widget.text())
        weight = float(self.vd_copper_weight_widget.text())
        converted_weight = convert_copper_weight(weight)

        # Calculate Internal Trace Resistance

        if self.vd_internal_width_widget.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.vd_internal_width_widget.text())

        internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width, converted_weight)

        vd_internal_resistance = calc_internal_trace_resistance(length,internal_actual_trace_area,temp_ambient)

        self.internal_resistance_widget.setText(str(vd_internal_resistance))

        # Calculate Internal Trace Voltage Drop
        voltage_drop_internal = calc_internal_trace_voltage_drop(amps,vd_internal_resistance)

        self.internal_drop_widget.setText(str(voltage_drop_internal))

        # Calculate External Trace Resistance

        if self.vd_external_width_widget.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.vd_external_width_widget.text())

        external_actual_trace_area = calc_internal_trace_area_actual(actual_external_trace_width, converted_weight)

        vd_external_resistance = calc_external_trace_resistance(length,external_actual_trace_area,temp_ambient)

        self.external_resistance_widget.setText(str(vd_external_resistance))

        # Calculate External Trace Voltage Drop
        voltage_drop_external = calc_external_trace_voltage_drop(amps,vd_external_resistance)

        self.external_drop_widget.setText(str(voltage_drop_external))

    def run_impedance_calc(self):

        epsilon_r = float(self.epsilon_r_widget.text())
        height = float(self.dielectric_height_widget.text())
        width = float(self.trace_width_widget.text())

        thickness = calc_total_thickness(float(self.base_weight_widget.text()),float(self.plating_weight_widget.text()))

        effective_epsilon = calc_epsilon_effective(epsilon_r,height,width)

        effective_width = calc_width_effective(width,thickness,height)


    def toggle_external_width(self, checked):

        self.external_trace_width_edit_widget.setVisible(not checked)

        self.external_trace_width_widget.setVisible(not checked)

        self.external_trace_area_widget.setVisible(not checked)

        self.external_actual_trace_area_widget.setVisible(not checked)

    def toggle_internal_width(self, checked):

        self.internal_trace_width_edit_widget.setVisible(not checked)

        self.internal_trace_width_widget.setVisible(not checked)

        self.internal_trace_area_widget.setVisible(not checked)

        self.internal_actual_trace_area_widget.setVisible(not checked)

    def toggle_external_vd_ohms(self, checked):

        self.vd_external_width_widget.setVisible(not checked)

        self.external_resistance_widget.setVisible(not checked)

        self.external_drop_widget.setVisible(not checked)

    def toggle_internal_vd_ohms(self, checked):

        self.vd_internal_width_widget.setVisible(not checked)

        self.internal_resistance_widget.setVisible(not checked)

        self.internal_drop_widget.setVisible(not checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidgetApp()
    window.show()
    sys.exit(app.exec())

