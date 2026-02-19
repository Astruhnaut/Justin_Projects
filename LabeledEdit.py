from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit


class LabeledLineEdit(QWidget):
    def __init__(self, label_text, width=75, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.label = QLabel(label_text)
        self.line_edit = QLineEdit()
        self.line_edit.setFixedWidth(width)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def text(self):
        return self.line_edit.text()

    def setText(self, value):
        self.line_edit.setText(value)

    def setPlaceholder(self, text):
        self.line_edit.setPlaceholderText(text)