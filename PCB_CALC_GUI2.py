import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, \
    QFormLayout, QMainWindow, QSpacerItem, QSizePolicy, QTabWidget, QCheckBox
from PyQt6.QtCore import Qt
from main import *

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
        epsilon_r_hbox = QHBoxLayout()
        epsilon_r_label = QLabel("Relative Permittivity")
        self.epsilon_r_edit = QLineEdit()
        self.epsilon_r_edit.setFixedWidth(75)

        epsilon_r_hbox.addWidget(epsilon_r_label)
        epsilon_r_hbox.addWidget(self.epsilon_r_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(epsilon_r_hbox)

        # Dielectric Height Input
        dielectric_height_hbox = QHBoxLayout()
        dielectric_height_label = QLabel("Dielectric Height (mils)")
        self.dielectric_height_edit = QLineEdit()
        self.dielectric_height_edit.setFixedWidth(75)

        dielectric_height_hbox.addWidget(dielectric_height_label)
        dielectric_height_hbox.addWidget(self.dielectric_height_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(dielectric_height_hbox)

        # Base Copper Weight Input
        base_weight_hbox = QHBoxLayout()
        base_weight_label = QLabel("Base Copper Weight (oz/ft^2)")
        self.base_weight_edit = QLineEdit()
        self.base_weight_edit.setFixedWidth(75)

        base_weight_hbox.addWidget(base_weight_label)
        base_weight_hbox.addWidget(self.base_weight_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(base_weight_hbox)

        # Plating Weight Input
        plating_weight_hbox = QHBoxLayout()
        plating_weight_label = QLabel("Plating Copper Weight (oz/ft^2)")
        self.plating_weight_edit = QLineEdit()
        self.plating_weight_edit.setFixedWidth(75)

        plating_weight_hbox.addWidget(plating_weight_label)
        plating_weight_hbox.addWidget(self.plating_weight_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(plating_weight_hbox)

        # Trace Width Input
        trace_width_hbox = QHBoxLayout()
        trace_width_label = QLabel("Trace Width (mils)")
        self.trace_width_edit = QLineEdit()
        self.trace_width_edit.setFixedWidth(75)

        trace_width_hbox.addWidget(trace_width_label)
        trace_width_hbox.addWidget(self.trace_width_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(trace_width_hbox)

        # Trace Spacing Input
        trace_spacing_hbox = QHBoxLayout()
        trace_spacing_label = QLabel("Trace Spacing (mils)")
        self.trace_spacing_edit = QLineEdit()
        self.trace_spacing_edit.setFixedWidth(75)

        trace_spacing_hbox.addWidget(trace_spacing_label)
        trace_spacing_hbox.addWidget(self.trace_spacing_edit)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(trace_spacing_hbox)


        # *******RESULTS*******

        # Create a spacer between INPUTS and RESULTS
        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        diff_pair_tab_layout.addItem(spacer)

        label_results = QLabel("RESULTS")
        label_results.setAlignment(Qt.AlignmentFlag.AlignCenter)

        diff_pair_tab_layout.addWidget(label_results)

        # Effective Permittivity Result
        epsilon_eff_hbox = QHBoxLayout()
        epsilon_eff_label = QLabel("Effective Permittivity")
        self.epsilon_eff_result = QLineEdit()
        self.epsilon_eff_result.setReadOnly(True)
        self.epsilon_eff_result.setFixedWidth(75)

        epsilon_eff_hbox.addWidget(epsilon_eff_label)
        epsilon_eff_hbox.addWidget(self.epsilon_eff_result)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(epsilon_eff_hbox)

        # Effective Trace Width Result
        width_eff_hbox = QHBoxLayout()
        width_eff_label = QLabel("Effective Trace Width (mils)")
        self.width_eff_result = QLineEdit()
        self.width_eff_result.setReadOnly(True)
        self.width_eff_result.setFixedWidth(75)

        width_eff_hbox.addWidget(width_eff_label)
        width_eff_hbox.addWidget(self.width_eff_result)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(width_eff_hbox)

        # Single Trace Impedance Result
        single_trace_impedance_hbox = QHBoxLayout()
        single_trace_impedance_label = QLabel("Single Trace Impedance (Ohms)")
        self.single_trace_impedance_result = QLineEdit()
        self.single_trace_impedance_result.setReadOnly(True)
        self.single_trace_impedance_result.setFixedWidth(75)

        single_trace_impedance_hbox.addWidget(single_trace_impedance_label)
        single_trace_impedance_hbox.addWidget(self.single_trace_impedance_result)

        # Add horizontal layout to the main vertical layout
        diff_pair_tab_layout.addLayout(single_trace_impedance_hbox)





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

        amps_hbox = QHBoxLayout()
        amps_label = QLabel("Desired Trace Current in Amps")
        self.amps_edit = QLineEdit()
        self.amps_edit.setFixedWidth(75)

        amps_hbox.addWidget(amps_label)
        amps_hbox.addWidget(self.amps_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(amps_hbox)

        internal_width_hbox = QHBoxLayout()
        self.internal_width_label = QLabel("INTERNAL Trace Width in mils")
        self.internal_width_edit = QLineEdit()
        self.internal_width_edit.setFixedWidth(75)

        internal_width_hbox.addWidget(self.internal_width_label)
        internal_width_hbox.addWidget(self.internal_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_width_hbox)

        external_width_hbox = QHBoxLayout()
        self.external_width_label = QLabel("EXTERNAL Trace Width in mils")
        self.external_width_edit = QLineEdit()
        self.external_width_edit.setFixedWidth(75)

        external_width_hbox.addWidget(self.external_width_label)
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
        self.internal_trace_width_label = QLabel("INTERNAL Minimum Trace Width in mils")
        self.min_trace_width_internal_result = QLineEdit()
        self.min_trace_width_internal_result.setReadOnly(True)
        self.min_trace_width_internal_result.setFixedWidth(75)

        internal_trace_width_hbox.addWidget(self.internal_trace_width_label)
        internal_trace_width_hbox.addWidget(self.min_trace_width_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_trace_width_hbox)

        internal_min_area_hbox = QHBoxLayout()
        self.internal_min_area_label = QLabel("INTERNAL Minimum Trace Area in mils^2")
        self.min_trace_area_internal_result = QLineEdit()
        self.min_trace_area_internal_result.setReadOnly(True)
        self.min_trace_area_internal_result.setFixedWidth(75)

        internal_min_area_hbox.addWidget(self.internal_min_area_label)
        internal_min_area_hbox.addWidget(self.min_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_min_area_hbox)

        internal_actual_area_hbox = QHBoxLayout()
        self.internal_actual_area_label = QLabel("INTERNAL Actual Trace Area in mils^2")
        self.actual_trace_area_internal_result = QLineEdit()
        self.actual_trace_area_internal_result.setReadOnly(True)
        self.actual_trace_area_internal_result.setFixedWidth(75)

        internal_actual_area_hbox.addWidget(self.internal_actual_area_label)
        internal_actual_area_hbox.addWidget(self.actual_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_actual_area_hbox)

        external_trace_width_hbox = QHBoxLayout()
        self.external_trace_width_label = QLabel("EXTERNAL Minimum Trace Width in mils")
        self.min_trace_width_external_result = QLineEdit()
        self.min_trace_width_external_result.setReadOnly(True)
        self.min_trace_width_external_result.setFixedWidth(75)

        external_trace_width_hbox.addWidget(self.external_trace_width_label)
        external_trace_width_hbox.addWidget(self.min_trace_width_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_trace_width_hbox)

        external_min_area_hbox = QHBoxLayout()
        self.external_min_area_label = QLabel("EXTERNAL Minimum Trace Area in mils^2")
        self.min_trace_area_external_result = QLineEdit()
        self.min_trace_area_external_result.setReadOnly(True)
        self.min_trace_area_external_result.setFixedWidth(75)

        external_min_area_hbox.addWidget(self.external_min_area_label)
        external_min_area_hbox.addWidget(self.min_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_min_area_hbox)

        external_actual_area_hbox = QHBoxLayout()
        self.external_actual_area_label = QLabel("EXTERNAL Actual Trace Area in mils^2")
        self.actual_trace_area_external_result = QLineEdit()
        self.actual_trace_area_external_result.setReadOnly(True)
        self.actual_trace_area_external_result.setFixedWidth(75)

        external_actual_area_hbox.addWidget(self.external_actual_area_label)
        external_actual_area_hbox.addWidget(self.actual_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_actual_area_hbox)

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
        amps = float(self.amps_edit.text())
        temp_rise_C = float(self.temp_rise_edit.text())

        min_trace_area_internal = calc_internal_trace_area_min(amps, temp_rise_C)

        self.min_trace_area_internal_result.setText(str(min_trace_area_internal))

        # Calculate Minimum External Trace Area
        min_trace_area_external = calc_external_trace_area_min(amps, temp_rise_C)

        self.min_trace_area_external_result.setText(str(min_trace_area_external))

        # Calculate Internal Actual Trace Area
        weight = float(self.copper_weight_edit.text())
        converted_weight = convert_copper_weight(weight)

        if self.internal_width_edit.text() == "":
            actual_internal_trace_width = 1
        else:
            actual_internal_trace_width = float(self.internal_width_edit.text())

        internal_actual_trace_area = calc_internal_trace_area_actual(actual_internal_trace_width, converted_weight)

        self.actual_trace_area_internal_result.setText(str(internal_actual_trace_area))

        # Calculate External Actual Trace Area
        if self.external_width_edit.text() == "":
            actual_external_trace_width = 1
        else:
            actual_external_trace_width = float(self.external_width_edit.text())

        external_actual_trace_area = calc_external_trace_area_actual(actual_external_trace_width, converted_weight)

        self.actual_trace_area_external_result.setText(str(external_actual_trace_area))

        # Calculate Minimum Internal Trace Width
        internal_trace_width = calc_min_trace_width_internal(min_trace_area_internal, converted_weight)

        self.min_trace_width_internal_result.setText(str(internal_trace_width))

        # Calculate Minimum External Trace Width
        external_trace_width = calc_min_trace_width_external(min_trace_area_external, converted_weight)

        self.min_trace_width_external_result.setText(str(external_trace_width))

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

        epsilon_r = float(self.epsilon_r_edit.text())
        height = float(self.dielectric_height_edit.text())
        width = float(self.trace_width_edit.text())

        thickness = calc_total_thickness(float(self.base_weight_edit.text()),float(self.plating_weight_edit.text()))

        effective_epsilon = calc_epsilon_effective(epsilon_r,height,width)

        effective_width = calc_width_effective(width,thickness,height)


    def toggle_external_width(self, checked):

        self.external_width_label.setVisible(not checked)
        self.external_width_edit.setVisible(not checked)

        self.external_trace_width_label.setVisible(not checked)
        self.min_trace_width_external_result.setVisible(not checked)

        self.external_min_area_label.setVisible(not checked)
        self.min_trace_area_external_result.setVisible(not checked)

        self.external_actual_area_label.setVisible(not checked)
        self.actual_trace_area_external_result.setVisible(not checked)

    def toggle_internal_width(self, checked):

        self.internal_width_label.setVisible(not checked)
        self.internal_width_edit.setVisible(not checked)

        self.internal_trace_width_label.setVisible(not checked)
        self.min_trace_width_internal_result.setVisible(not checked)

        self.internal_min_area_label.setVisible(not checked)
        self.min_trace_area_internal_result.setVisible(not checked)

        self.internal_actual_area_label.setVisible(not checked)
        self.actual_trace_area_internal_result.setVisible(not checked)

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

