from lib.signal import Signal
from time import time
import os


class Usb:
    dir = "/dev"
    usb_pattern = "ttyUSB"
    usb_name = ""
    ls_and_grep_cmd = "ls {} | grep {}"
    signal = False

    action_codes = []
    errors = []
    last_setup_time = 0
    setup_interval = 1.5

    def __init__(self):
        self.ls_and_grep_cmd = self.ls_and_grep_cmd.format(self.dir, self.usb_pattern)

    def setup(self, usb_name):
        if self.last_setup():
            self.last_setup_time = time()
            self.usb_name = usb_name
            self.signal = Signal(self.tty_usb_name(), self)
            self.signal.start()
            return True
        return False

    def last_setup(self):
        if time() - self.last_setup_time > self.setup_interval:
            return True
        return False

    def tty_usb_name(self):
        return self.dir + "/" + self.usb_name

    def get_codes(self):
        codes = self.action_codes
        self.action_codes = []
        return codes

    def get_errors(self):
        errors = self.errors
        self.errors = []
        return errors

    def find(self):
        tty_usb = self.find_usb()
        if self.usb_pattern in tty_usb:
            return tty_usb
        return False

    def find_usb(self):
        tty_usb = os.popen(self.ls_and_grep_cmd).read().strip(' \t\n\r')
        return str(tty_usb)

