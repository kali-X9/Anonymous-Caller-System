import subprocess
import time
import asyncio
from src.logger import setup_logger

logger = setup_logger(__name__)

async def enable_tor_vpn():
    logger.info("Starting Tor & VPN services...")
    try:
        subprocess.run(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["service", "openvpn", "start"], check=True)
        await asyncio.sleep(10)
        logger.info("Tor & VPN activated successfully.")
    except Exception as e:
        logger.error(f"Failed to enable anonymity: {e}")
        raise

async def auto_change_ip(interval=10):
    while True:
        try:
            subprocess.run(["service", "tor", "restart"], check=True)
            logger.info("IP changed via Tor.")
        except Exception as e:
            logger.warning(f"Failed to restart Tor: {e}")
        await asyncio.sleep(interval)
