import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette


class MonitorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PiVital - Tempus Pro Simulator")
        self.setGeometry(100, 100, 1024, 600)
        self.setStyleSheet("background-color: black; color: white;")
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # --- VITALS TOP ROW ---
        vitals_layout = QHBoxLayout()
        vitals = [
            ("HR", "###", "red"),
            ("BP", "###/##", "green"),
            ("SpO₂", "##%", "blue"),
            ("ETCO₂", "## mmHg", "yellow"),
            ("Temp", "##.# °C", "orange"),
        ]
        for label, value, color in vitals:
            vitals_layout.addWidget(self.create_vital_box(label, value, color))

        # --- WAVEFORM PLACEHOLDERS ---
        waveforms_layout = QVBoxLayout()
        waveforms = ["Lead II", "SpO₂", "ETCO₂"]
        for title in waveforms:
            waveforms_layout.addWidget(self.create_waveform_box(title))

        # --- BOTTOM MENU BUTTONS ---
        button_layout = QHBoxLayout()
        buttons = ["Alarm Silence", "Home", "Export", "Display Menu", "Patient Menu"]
        for text in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("font-size: 16px; background-color: #444; color: white;")
            btn.setFixedHeight(50)
            button_layout.addWidget(btn)

        # --- FINAL ASSEMBLY ---
        main_layout.addLayout(vitals_layout)
        main_layout.addLayout(waveforms_layout)
        main_layout.addStretch()
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def create_vital_box(self, label, value, color_name):
        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setStyleSheet(f"border: 2px solid {color_name};")
        layout = QVBoxLayout()

        lbl_label = QLabel(label)
        lbl_label.setFont(QFont("Arial", 14, QFont.Bold))
        lbl_label.setAlignment(Qt.AlignCenter)

        lbl_value = QLabel(value)
        lbl_value.setFont(QFont("Arial", 24, QFont.Bold))
        lbl_value.setAlignment(Qt.AlignCenter)
        lbl_value.setStyleSheet(f"color: {color_name};")

        layout.addWidget(lbl_label)
        layout.addWidget(lbl_value)
        frame.setLayout(layout)
        frame.setFixedWidth(150)
        return frame

    def create_waveform_box(self, title):
        label = QLabel(f"{title} waveform area")
        label.setFixedHeight(80)
        label.setFont(QFont("Courier", 12))
        label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        label.setStyleSheet("border: 1px solid gray; background-color: #111; color: white; padding: 5px;")
        return label


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonitorWindow()
    window.show()
    sys.exit(app.exec_())