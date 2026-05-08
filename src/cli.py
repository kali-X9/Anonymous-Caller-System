import click
from src.security.anonymity import enable_tor_vpn, auto_change_ip
from src.security.mac_spoof import spoof_mac
from src.security.sip_caller import make_call
from src.logger import setup_logger
import asyncio

logger = setup_logger(__name__)

@click.command()
@click.option('--call', '-c', help='Phone number to call anonymously')
def main(call):
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(enable_tor_vpn())
        spoof_mac()
        if call:
            make_call(call)
        else:
            number = input("Enter phone number to call anonymously: ")
            make_call(number)
        loop.create_task(auto_change_ip())
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info("Gracefully shutting down...")
    except Exception as e:
        logger.critical(f"Critical error occurred: {e}")

if __name__ == "__main__":
    main()
