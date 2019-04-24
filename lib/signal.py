import threading
import serial


class Signal(threading.Thread):
    def __init__(self, tty_usb, master):
        self.serial = serial.Serial(tty_usb, 9600)
        threading.Thread.__init__(self)
        self.master = master
        self.last_valid_code = b''
        self.empty_code = b'FFFFFFFF'
        self.empty_code_as_last_valid = False

    def run(self):
        while True:
            try:
                code = self.serial.readline().strip()
                self.append_code(code)
            except Exception as ex:
                self.master.errors.append(ex)
                break

    def append_code(self, code):
        if code != self.empty_code:
            self.last_valid_code = code
            self.empty_code_as_last_valid = False
            self.master.action_codes.append(code)
        elif self.empty_code_as_last_valid:
            self.master.action_codes.append(self.last_valid_code)
        else:
            self.empty_code_as_last_valid = True
