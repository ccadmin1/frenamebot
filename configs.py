# (c) @TumaraBaap • @RymOfficial

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = "9244035"
    API_HASH = "66c62a85cfbf593a991ea680223a0549"
    BOT_TOKEN = "5062336126:AAE_8j8jCft2ZC17pXSiET7_dU_myDvMLp8"
    DOWNLOAD_DIR = "./downloads"
    LOGGER = logging
    OWNER_ID = "5088475411"
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = "mongodb+srv://Aj:Aj@cluster0.pvz0y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    LOG_CHANNEL = "-1001673475040"
    BROADCAST_AS_COPY = "False"
