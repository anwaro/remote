import threading
import serial


class Signal(threading.Thread):
    def __init__(self, tty_usb, master):
        self.serial = serial.Serial(tty_usb, 9600)
        threading.Thread.__init__(self)
        self.master = master

    def run(self):
        while True:
            try:
                signal = self.serial.readline().strip()
                self.master.action_codes.append(signal)
            except Exception as ex:
                self.master.errors.append(ex)
                break
