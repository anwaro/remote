from datetime import datetime


class Logger:
    INFO = 'INFO'
    ERROR = 'ERROR'

    dir = "log/"
    error_log_file = 'error.log'
    system_log_file = 'system.log'

    @staticmethod
    def log(msg, save=False, level=None):
        level = Logger.INFO if level is None else level
        Logger.log_msg(msg, Logger.system_log_file, save, level)

    @staticmethod
    def error(msg):
        if type(msg) == list:
            for i in msg:
                Logger.log_msg(i, Logger.error_log_file, True, Logger.ERROR)
        else:
            Logger.log_msg(msg, Logger.error_log_file, True, Logger.ERROR)

    @staticmethod
    def log_msg(msg, file, save, level):
        msg = "[{}][{}]: {}".format(Logger.time(), level, msg)
        print(msg)
        if save:
            Logger.write(msg, file)

    @staticmethod
    def file_path(file):
        return Logger.dir + file

    @staticmethod
    def write(msg, file):
        file = open(Logger.file_path(file), "a")
        file.write(msg)
        file.close()

    @staticmethod
    def time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
