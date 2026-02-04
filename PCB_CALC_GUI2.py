import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFormLayout, QMainWindow, QSpacerItem, QSizePolicy, QTabWidget
from PyQt6.QtCore import Qt
from main import *

class TabWidgetApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCB DESIGN CALCULATOR")
        self.setGeometry(625, 100, 450, 800)

        # Set up layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Create the QTabWidget
        self.tabs = QTabWidget()
        self.main_layout.addWidget(self.tabs)

        self.central_widget.setStyleSheet("background-color: white;")

        # Create the trace width tab
        self.trace_width_tab = QWidget()
        self.tabs.addTab(self.trace_width_tab, "Trace Width")
        self.init_trace_width_tab_ui()

        # Create the trace resistance tab
        self.trace_resistance_tab = QWidget()
        self.tabs.addTab(self.trace_resistance_tab, "Trace Resistance")
        self.init_trace_resistance_tab_ui()

    def init_trace_width_tab_ui(self):

        trace_width_tab_layout = QVBoxLayout()
        self.trace_width_tab.setLayout(trace_width_tab_layout)

        #*******INPUTS*******

        label_inputs = QLabel("INPUTS")
        label_inputs.setAlignment(Qt.AlignmentFlag.AlignCenter)

        trace_width_tab_layout.addWidget(label_inputs)

        amps_hbox = QHBoxLayout()
        amps_label = QLabel("Desired Trace Current in Amps")
        amps_edit = QLineEdit()
        amps_edit.setFixedWidth(75)

        amps_hbox.addWidget(amps_label)
        amps_hbox.addWidget(amps_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(amps_hbox)

        internal_width_hbox = QHBoxLayout()
        internal_width_label = QLabel("INTERNAL Trace Width in mils")
        internal_width_edit = QLineEdit()
        internal_width_edit.setFixedWidth(75)

        internal_width_hbox.addWidget(internal_width_label)
        internal_width_hbox.addWidget(internal_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_width_hbox)

        external_width_hbox = QHBoxLayout()
        external_width_label = QLabel("EXTERNAL Trace Width in mils")
        external_width_edit = QLineEdit()
        external_width_edit.setFixedWidth(75)

        external_width_hbox.addWidget(external_width_label)
        external_width_hbox.addWidget(external_width_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_width_hbox)

        temp_rise_hbox = QHBoxLayout()
        temp_rise_label = QLabel("Temperature Rise in Celsius")
        temp_rise_edit = QLineEdit()
        temp_rise_edit.setFixedWidth(75)

        temp_rise_hbox.addWidget(temp_rise_label)
        temp_rise_hbox.addWidget(temp_rise_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(temp_rise_hbox)

        copper_weight_hbox = QHBoxLayout()
        copper_weight_label = QLabel("Copper Weight in oz/ft^2")
        copper_weight_edit = QLineEdit()
        copper_weight_edit.setFixedWidth(75)

        copper_weight_hbox.addWidget(copper_weight_label)
        copper_weight_hbox.addWidget(copper_weight_edit)

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
        min_trace_width_internal_result = QLineEdit()
        min_trace_width_internal_result.setReadOnly(True)
        min_trace_width_internal_result.setFixedWidth(75)

        internal_trace_width_hbox.addWidget(internal_trace_width_label)
        internal_trace_width_hbox.addWidget(min_trace_width_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_trace_width_hbox)

        internal_min_area_hbox = QHBoxLayout()
        internal_min_area_label = QLabel("INTERNAL Minimum Trace Area in mils^2")
        min_trace_area_internal_result = QLineEdit()
        min_trace_area_internal_result.setReadOnly(True)
        min_trace_area_internal_result.setFixedWidth(75)

        internal_min_area_hbox.addWidget(internal_min_area_label)
        internal_min_area_hbox.addWidget(min_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_min_area_hbox)

        internal_actual_area_hbox = QHBoxLayout()
        internal_actual_area_label = QLabel("INTERNAL Actual Trace Area in mils^2")
        actual_trace_area_internal_result = QLineEdit()
        actual_trace_area_internal_result.setReadOnly(True)
        actual_trace_area_internal_result.setFixedWidth(75)

        internal_actual_area_hbox.addWidget(internal_actual_area_label)
        internal_actual_area_hbox.addWidget(actual_trace_area_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(internal_actual_area_hbox)

        external_trace_width_hbox = QHBoxLayout()
        external_trace_width_label = QLabel("EXTERNAL Minimum Trace Width in mils")
        min_trace_width_external_result = QLineEdit()
        min_trace_width_external_result.setReadOnly(True)
        min_trace_width_external_result.setFixedWidth(75)

        external_trace_width_hbox.addWidget(external_trace_width_label)
        external_trace_width_hbox.addWidget(min_trace_width_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_trace_width_hbox)

        external_min_area_hbox = QHBoxLayout()
        external_min_area_label = QLabel("EXTERNAL Minimum Trace Area in mils^2")
        min_trace_area_external_result = QLineEdit()
        min_trace_area_external_result.setReadOnly(True)
        min_trace_area_external_result.setFixedWidth(75)

        external_min_area_hbox.addWidget(external_min_area_label)
        external_min_area_hbox.addWidget(min_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_min_area_hbox)

        external_actual_area_hbox = QHBoxLayout()
        external_actual_area_label = QLabel("EXTERNAL Actual Trace Area in mils^2")
        actual_trace_area_external_result = QLineEdit()
        actual_trace_area_external_result.setReadOnly(True)
        actual_trace_area_external_result.setFixedWidth(75)

        external_actual_area_hbox.addWidget(external_actual_area_label)
        external_actual_area_hbox.addWidget(actual_trace_area_external_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(external_actual_area_hbox)

        # Set the layout for the main window
        self.setLayout(trace_width_tab_layout)

        trace_width_tab_layout.addStretch()

    def init_trace_resistance_tab_ui(self):

        trace_resistance_tab_layout = QVBoxLayout()
        self.trace_resistance_tab.setLayout(trace_resistance_tab_layout)

        # --- First Row (Name) ---
        trace_resistance_hbox = QHBoxLayout()
        name_label = QLabel("INTERNAL Trace Resistance")
        name_edit = QLineEdit()
        trace_resistance_hbox.addWidget(name_label)
        trace_resistance_hbox.addWidget(name_edit)

        # Add horizontal layouts to the main vertical layout
        trace_resistance_tab_layout.addLayout(trace_resistance_hbox)

        # Set the layout for the main window
        self.setLayout(trace_resistance_tab_layout)

        trace_resistance_tab_layout.addStretch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabWidgetApp()
    window.show()
    sys.exit(app.exec())

