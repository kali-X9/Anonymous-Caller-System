import subprocess
from src.logger import setup_logger

logger = setup_logger(__name__)

def spoof_mac(interface="eth0"):
    try:
        logger.info(f"Changing MAC address for interface '{interface}'...")
        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["macchanger", "-r", interface], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)
        logger.info("MAC address successfully changed.")
    except Exception as e:
        logger.error(f"MAC spoofing failed: {e}")
        raise
