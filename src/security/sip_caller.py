import pjsua as pj
from src.config import config
from src.logger import setup_logger

logger = setup_logger(__name__)

class MyAccountCallback(pj.AccountCallback):
    def __init__(self, account):
        super().__init__(account)

    def on_incoming_call(self, call):
        logger.info("Incoming call detected. Answering...")
        call.answer(200)

def setup_secure_call():
    try:
        lib = pj.Lib()
        lib.init(log_cfg=pj.LogConfig(level=3))
        transport = lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(config['sip']['port']))
        lib.start()
        acc_cfg = pj.AccountConfig(
            domain=config['sip']['domain'],
            username=config['sip']['username'],
            password=config['sip']['password']
        )
        acc = lib.create_account(acc_cfg)
        acc_cb = MyAccountCallback(acc)
        acc.set_callback(acc_cb)
        logger.info("SIP account registered securely.")
        return lib
    except Exception as e:
        logger.error(f"SIP setup failed: {e}")
        raise

def make_call(number):
    try:
        lib = setup_secure_call()
        call = lib.create_call(number)
        call.connect()
        logger.info(f"Calling {number} securely...")
    except Exception as e:
        logger.error(f"Call failed: {e}")
        raise
