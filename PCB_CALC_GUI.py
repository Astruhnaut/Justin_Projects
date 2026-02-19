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

        self.internal_calc_checkbox = QCheckBox('Calc INTERNAL')
        self.internal_calc_checkbox.setChecked(False) # Initially NOT checked

        self.internal_calc_checkbox.toggled.connect(self.toggle_external_width)

        trace_width_tab_layout.addWidget(self.internal_calc_checkbox)

        self.external_calc_checkbox = QCheckBox('Calc EXTERNAL')
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

        self.internal_calc_checkbox2 = QCheckBox('Calc INTERNAL')
        self.internal_calc_checkbox2.setChecked(False) # Initially NOT checked

        self.internal_calc_checkbox2.toggled.connect(self.toggle_external_vd_ohms)

        trace_resistance_tab_layout.addWidget(self.internal_calc_checkbox2)

        self.external_calc_checkbox2 = QCheckBox('Calc EXTERNAL')
        self.external_calc_checkbox2.setChecked(False) # Initially NOT checked

        self.external_calc_checkbox2.toggled.connect(self.toggle_internal_vd_ohms)

        trace_resistance_tab_layout.addWidget(self.external_calc_checkbox2)

        # *******INPUTS*******

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_resistance_tab_layout.addWidget(label_inputs)

        vd_amps_hbox = QHBoxLayout()
        length_label = QLabel("Desired Current in Amps")
        self.vd_amps_edit = QLineEdit()
        self.vd_amps_edit.setFixedWidth(75)

        vd_amps_hbox.addWidget(length_label)
        vd_amps_hbox.addWidget(self.vd_amps_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(vd_amps_hbox)

        vd_internal_width_hbox = QHBoxLayout()
        self.vd_internal_width_label = QLabel("INTERNAL Trace Width in mils")
        self.vd_internal_width_edit = QLineEdit()
        self.vd_internal_width_edit.setFixedWidth(75)

        vd_internal_width_hbox.addWidget(self.vd_internal_width_label)
        vd_internal_width_hbox.addWidget(self.vd_internal_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(vd_internal_width_hbox)

        vd_external_width_hbox = QHBoxLayout()
        self.vd_external_width_label = QLabel("EXTERNAL Trace Width in mils")
        self.vd_external_width_edit = QLineEdit()
        self.vd_external_width_edit.setFixedWidth(75)

        vd_external_width_hbox.addWidget(self.vd_external_width_label)
        vd_external_width_hbox.addWidget(self.vd_external_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(vd_external_width_hbox)

        length_hbox = QHBoxLayout()
        length_label = QLabel("Actual Trace Length in mils")
        self.length_edit = QLineEdit()
        self.length_edit.setFixedWidth(75)

        length_hbox.addWidget(length_label)
        length_hbox.addWidget(self.length_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(length_hbox)

        ambient_temp_hbox = QHBoxLayout()
        ambient_temp_label = QLabel("Ambient Temp in Celsius")
        self.ambient_temp_edit = QLineEdit()
        self.ambient_temp_edit.setFixedWidth(75)

        ambient_temp_hbox.addWidget(ambient_temp_label)
        ambient_temp_hbox.addWidget(self.ambient_temp_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(ambient_temp_hbox)

        vd_copper_weight_hbox = QHBoxLayout()
        vd_copper_weight_label = QLabel("Copper Weight in oz/ft^2")
        self.vd_copper_weight_edit = QLineEdit()
        self.vd_copper_weight_edit.setFixedWidth(75)

        vd_copper_weight_hbox.addWidget(vd_copper_weight_label)
        vd_copper_weight_hbox.addWidget(self.vd_copper_weight_edit)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(vd_copper_weight_hbox)


        #*******RESULTS*******

        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        trace_resistance_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_resistance_tab_layout.addWidget(label_results)

        trace_resistance_internal_hbox = QHBoxLayout()
        self.internal_resistance_label = QLabel("INTERNAL Trace Resistance")
        self.internal_resistance_result = QLineEdit()
        self.internal_resistance_result.setReadOnly(True)
        self.internal_resistance_result.setFixedWidth(75)

        trace_resistance_internal_hbox.addWidget(self.internal_resistance_label)
        trace_resistance_internal_hbox.addWidget(self.internal_resistance_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_resistance_internal_hbox)

        trace_voltage_drop_internal_hbox = QHBoxLayout()
        self.internal_drop_label = QLabel("INTERNAL Trace Voltage Drop")
        self.internal_drop_result = QLineEdit()
        self.internal_drop_result.setReadOnly(True)
        self.internal_drop_result.setFixedWidth(75)

        trace_voltage_drop_internal_hbox.addWidget(self.internal_drop_label)
        trace_voltage_drop_internal_hbox.addWidget(self.internal_drop_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_voltage_drop_internal_hbox)

        trace_resistance_external_hbox = QHBoxLayout()
        self.external_resistance_label = QLabel("EXTERNAL Trace Resistance")
        self.external_resistance_result = QLineEdit()
        self.external_resistance_result.setReadOnly(True)
        self.external_resistance_result.setFixedWidth(75)

        trace_resistance_external_hbox.addWidget(self.external_resistance_label)
        trace_resistance_external_hbox.addWidget(self.external_resistance_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_resistance_external_hbox)

        trace_voltage_drop_external_hbox = QHBoxLayout()
        self.external_drop_label = QLabel("EXTERNAL Trace Voltage Drop")
        self.external_drop_result = QLineEdit()
        self.external_drop_result.setReadOnly(True)
        self.external_drop_result.setFixedWidth(75)

        trace_voltage_drop_external_hbox.addWidget(self.external_drop_label)
        trace_voltage_drop_external_hbox.addWidget(self.external_drop_result)

        # Add horizontal layout to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_voltage_drop_external_hbox)

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

        amps = float(self.vd_amps_edit.text())
        length = float(self.length_edit.text())
        temp_ambient = float(self.ambient_temp_edit.text())
        weight = float(self.vd_copper_weight_edit.text())
        converted_weight = convert_copper_weight(weight)

        # Calculate Internal Trace Resistance

        if self.vd_internal_width_edit.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.vd_internal_width_edit.text())

        internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width, converted_weight)

        vd_internal_resistance = calc_internal_trace_resistance(length,internal_actual_trace_area,temp_ambient)

        self.internal_resistance_result.setText(str(vd_internal_resistance))

        # Calculate Internal Trace Voltage Drop
        voltage_drop_internal = calc_internal_trace_voltage_drop(amps,vd_internal_resistance)

        self.internal_drop_result.setText(str(voltage_drop_internal))

        # Calculate External Trace Resistance

        if self.vd_external_width_edit.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.vd_external_width_edit.text())

        external_actual_trace_area = calc_internal_trace_area_actual(actual_external_trace_width, converted_weight)

        vd_external_resistance = calc_external_trace_resistance(length,external_actual_trace_area,temp_ambient)

        self.external_resistance_result.setText(str(vd_external_resistance))

        # Calculate External Trace Voltage Drop
        voltage_drop_external = calc_external_trace_voltage_drop(amps,vd_external_resistance)

        self.external_drop_result.setText(str(voltage_drop_external))

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

        self.vd_external_width_label.setVisible(not checked)
        self.vd_external_width_edit.setVisible(not checked)

        self.external_resistance_label.setVisible(not checked)
        self.external_resistance_result.setVisible(not checked)

        self.external_drop_label.setVisible(not checked)
        self.external_drop_result.setVisible(not checked)

    def toggle_internal_vd_ohms(self, checked):

        self.vd_internal_width_label.setVisible(not checked)
        self.vd_internal_width_edit.setVisible(not checked)

        self.internal_resistance_label.setVisible(not checked)
        self.internal_resistance_result.setVisible(not checked)

        self.internal_drop_label.setVisible(not checked)
        self.internal_drop_result.setVisible(not checked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidgetApp()
    window.show()
    sys.exit(app.exec())

