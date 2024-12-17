import time
import sys
from pathlib import Path

# now
from datetime import datetime
now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# do logging stuff
import logging
logger = logging.getLogger()

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

LOG_FILENAME = f"matrix-mbt{now}.log"
LOG_FOLDER = "log"
LOG_FILE = Path(f"{LOG_FOLDER}/{LOG_FILENAME}")

# import from own libraries
from matrix_user import MatrixUser


# TO BE TAKEN FROM CONFIG:
SERVER_PORT = "8008"
SERVER_ADDRESS = "localhost"
SERVER_NAME = "variability.testing.nl"
SERVER_PROTOCOL = "http"
SERVER = SERVER_PROTOCOL + "://" + SERVER_ADDRESS + ":" + SERVER_PORT

USERNAME = "testUser111"
PASSWORD = "aAAlff134Z!F?3dkldfa"

TESTROOM_ID = "!AxPlfhgsOJxRiKuOWe:variability.testing.nl"

def main():
    # check if the file exists and if not create it
    LOG_FILE.parent.mkdir(exist_ok=True, parents=True)
    LOG_FILE.touch()
    # set basic config for logging as specified at top of file
    logging.basicConfig(filename=LOG_FILE, 
                        level=LOG_LEVEL,
                        format=LOG_FORMAT)
    # add handler to the logger to also print logs in the stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.info("initialized logging")

    user = MatrixUser(SERVER, USERNAME, PASSWORD)
    user.login()
    time.sleep(0.5)
    user.send_message(TESTROOM_ID, "some Message")
    time.sleep(0.5)
    user.leave_room(TESTROOM_ID)
    time.sleep(0.5)
    user.join_room(TESTROOM_ID)
    time.sleep(0.5)
    user.send_message(TESTROOM_ID, "am back")

if __name__ == '__main__':
    main()
