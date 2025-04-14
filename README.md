# PiVital

**PiVital** is a Raspberry Pi-based simulation of the RDT Tempus Pro cardiac monitor for use in EMS and austere medicine training environments. It features a realistic graphical interface, vital sign simulation, waveform display, and instructor-controlled patient profiles.

## Key Features
- Realistic GUI mimicking the Tempus Pro monitor
- Vital sign and waveform display with dynamic updates
- Instructor web interface for scenario control and data injection
- Support for multi-patient expansion and scenario recording

## Tech Stack
- **Hardware:** Raspberry Pi 3B+ or 4B, 10" touchscreen
- **Frontend:** PyQt5 for GUI
- **Backend:** Flask for instructor interface
- **Data:** JSON-based scenario profiles

## Folder Structure
- `main.py` – Student-facing monitor GUI
- `instructor_server.py` – Web control panel for instructors
- `profiles.py` – Vital sign presets and scenario data
- `assets/` – Images, waveforms, logos, and sounds
- `utils/` – Helper scripts (e.g., data management)
- `requirements.txt` – Python dependencies

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/PiVital.git
cd PiVital
pip install -r requirements.txt
python3 main.py