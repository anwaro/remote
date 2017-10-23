import sys
import os


class Helper:
    @staticmethod
    def app_path():
        pathname = os.path.dirname(sys.argv[0])
        return os.path.abspath(pathname)
