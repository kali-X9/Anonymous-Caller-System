#!/bin/bash
set -e

echo "[+] Installing system dependencies..."
sudo apt update
sudo apt install -y python3-pip tor openvpn macchanger

echo "[+] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[+] Setup completed."
