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

        # === 1. Most recommended for forms: QFormLayout ===
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setSpacing(8)

        self.amps_edit = QLineEdit()
        self.amps_edit.setFixedWidth(75)
        self.length_edit = QLineEdit()
        self.length_edit.setFixedWidth(75)
        self.temp_rise_edit = QLineEdit()
        self.temp_rise_edit.setFixedWidth(75)
        self.copper_weight_edit = QLineEdit()
        self.copper_weight_edit.setFixedWidth(75)
        self.ambient_temp_edit = QLineEdit()
        self.ambient_temp_edit.setFixedWidth(75)
        self.trace_width_edit = QLineEdit()
        self.trace_width_edit.setFixedWidth(75)

        self.calculate = QPushButton("Calculate")
        self.calculate.clicked.connect(self.run_calc)

        form_layout.addRow("Desired Trace Current in Amps", self.amps_edit)
        form_layout.addRow("Trace Length in mils", self.length_edit)
        form_layout.addRow("Temp Rise in Deg C", self.temp_rise_edit)
        form_layout.addRow("Copper Weight in oz/ft^2", self.copper_weight_edit)
        form_layout.addRow("Ambient Temperature in Deg C", self.ambient_temp_edit)
        form_layout.addRow("Trace Width in mils", self.trace_width_edit)

        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.calculate)

        # Connect the textChanged signal to the update_variable function
        self.amps_edit.textChanged.connect(self.update_variable)

        # Connect the textChanged signal to the update_variable function
        self.length_edit.textChanged.connect(self.update_variable)

        # Connect the textChanged signal to the update_variable function
        self.temp_rise_edit.textChanged.connect(self.update_variable)

        # Connect the textChanged signal to the update_variable function
        self.copper_weight_edit.textChanged.connect(self.update_variable)

        # Connect the textChanged signal to the update_variable function
        self.ambient_temp_edit.textChanged.connect(self.update_variable)

        # Connect the textChanged signal to the update_variable function
        self.trace_width_edit.textChanged.connect(self.update_variable)

    def update_variable(self, text):
        """
        This function is called automatically every time the text changes.
        """
        self.user_input = text

    def run_calc(self):

        amps = float(self.amps_edit.text())
        temp_rise_C = float(self.temp_rise_edit.text())

        min_trace_area = calc_trace_area_min(amps,temp_rise_C)

        print(f"Minimum trace area: {min_trace_area} mils^2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormWindow()
    window.show()
    sys.exit(app.exec())

