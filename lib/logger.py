from datetime import datetime
import logging


class Logger:
    LOG = 1

    @staticmethod
    def log(msg):
        print("[" + Logger.time() + "]: ", msg)

    @staticmethod
    def error(msg):
        logging.basicConfig(filename='log/error.log', level=logging.ERROR)
        if type(msg) == list:
            for i in msg:
                logging.error(i)
        else:
            logging.error(msg)

    @staticmethod
    def time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
