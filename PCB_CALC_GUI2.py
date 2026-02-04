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

        amps_hbox = QHBoxLayout()
        amps_label = QLabel("Enter Desired Trace Current")
        amps_edit = QLineEdit()
        amps_edit.setFixedWidth(75)

        amps_hbox.addWidget(amps_label)
        amps_hbox.addWidget(amps_edit)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(amps_hbox)

        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        trace_width_tab_layout.addItem(spacer)

        trace_width_hbox = QHBoxLayout()
        trace_width_label = QLabel("INTERNAL Minimum Trace Width")
        min_trace_width_internal_result = QLineEdit()
        min_trace_width_internal_result.setReadOnly(True)
        min_trace_width_internal_result.setFixedWidth(75)

        trace_width_hbox.addWidget(trace_width_label)
        trace_width_hbox.addWidget(min_trace_width_internal_result)

        # Add horizontal layout to the main vertical layout
        trace_width_tab_layout.addLayout(trace_width_hbox)

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

