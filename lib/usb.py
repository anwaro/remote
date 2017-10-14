from lib.signal import Signal
import os


class Usb:
    dir = "/dev"
    usb_pattern = "ttyUSB"
    usb_name = ""
    ls_and_grep_cmd = "ls {} | grep {}"
    signal = False

    action_codes = []
    errors = []

    def __init__(self):
        self.ls_and_grep_cmd = self.ls_and_grep_cmd.format(self.dir, self.usb_pattern)

    def setup(self, usb_name):
        self.usb_name = usb_name
        self.signal = Signal(self.tty_usb_name(), self)
        self.signal.start()

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

