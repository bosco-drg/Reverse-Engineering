# 🔬 USB Hacking – Aaronia BPSG 6 Signal Generator

This project aims to reverse engineer the USB communication protocol used by the Aaronia BPSG 6 RF signal generator. The manufacturer does not provide any API documentation, and the official software is only available for x86 platforms with a GUI, making it unsuitable for headless systems like Raspberry Pi. Our goal is to create an open-source command-line tool (in Python) to control basic features of the generator (frequency, output power) via USB, making it accessible for remote or embedded applications.

🚀 **Goals**
- Understand the USB protocol used by the BPSG 6
- Capture and analyze USB packets from the proprietary software
- Develop a cross-platform Python interface to control the generator
- Allow usage from headless or ARM-based systems (e.g., Raspberry Pi)

🔧 Tools used: `Wireshark`, `usbmon`, `PyUSB`, `lsusb`, `dmesg`

This project is for educational purposes and is not affiliated with Aaronia AG.
