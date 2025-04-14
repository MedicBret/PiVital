import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton, QFrame
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class MonitorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PiVital - Tempus Pro Simulator")
        self.setGeometry(100, 100, 1024, 600)
        self.setStyleSheet("background-color: black; color: white;")
        self.vital_labels = {}
        self.vital_index = 0
        self.vital_data = [
            {"HR": "82", "BP": "120/80", "SpO2": "98%", "ETCO2": "36 mmHg", "Temp": "37.0 °C"},
            {"HR": "110", "BP": "100/60", "SpO2": "94%", "ETCO2": "40 mmHg", "Temp": "38.1 °C"},
            {"HR": "130", "BP": "88/56", "SpO2": "90%", "ETCO2": "45 mmHg", "Temp": "38.9 °C"},
            {"HR": "160", "BP": "70/40", "SpO2": "84%", "ETCO2": "50 mmHg", "Temp": "39.4 °C"},
            {"HR": "98", "BP": "110/70", "SpO2": "96%", "ETCO2": "38 mmHg", "Temp": "37.4 °C"}
        ]
        self.init_ui()
        self.start_timer()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # --- VITALS TOP ROW ---
        vitals_layout = QHBoxLayout()
        vitals = [
            ("HR", "red"),
            ("BP", "green"),
            ("SpO2", "blue"),
            ("ETCO2", "yellow"),
            ("Temp", "orange"),
        ]
        for label, color in vitals:
            vital_box = self.create_vital_box(label, "--", color)
            self.vital_labels[label] = vital_box.findChild(QLabel, f"value_{label}")
            vitals_layout.addWidget(vital_box)

        # --- WAVEFORM PLACEHOLDERS ---
        waveforms_layout = QVBoxLayout()
        waveforms = ["Lead II", "SpO2", "ETCO2"]
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
        lbl_value.setObjectName(f"value_{label}")
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

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_vitals)
        self.timer.start(1000)  # Update every 1 second

    def update_vitals(self):
        vitals = self.vital_data[self.vital_index]
        for key, value in vitals.items():
            if key in self.vital_labels:
                self.vital_labels[key].setText(value)
        self.vital_index = (self.vital_index + 1) % len(self.vital_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonitorWindow()
    window.show()
    sys.exit(app.exec_())