# from lib.window import Window
from lib.logger import Logger
from lib.mainloop import MainLoop
from lib.usb import Usb


class RemoteApp:
    usb_active = False
    remote = False

    def __init__(self):
        self.logger = Logger()
        # self.window = Window()
        self.main_loop = MainLoop()
        self.usb = Usb()
        Logger.log('Init RemoteApp')

    def run(self):
        self.main_loop.set_interval(self.main, 1)
        # self.window.run()

    def find_usb_device(self):
        tty_usb = self.usb.find()
        if tty_usb:
            try:
                self.usb.setup(tty_usb)
                self.usb_active = True
            except Exception as error:
                Logger.error(error)

    def remote_action(self):
        error = self.usb.get_errors()
        if len(error):
            Logger.error(error)
            self.usb_active = False
        else:
            action_codes = self.usb.get_codes()

    def main(self):
        if not self.usb_active:
            self.find_usb_device()
        else:
            self.remote_action()


if __name__ == "__main__":
    app = RemoteApp()
    app.run()
