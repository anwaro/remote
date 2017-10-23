from lib.logger import Logger
from lib.mainloop import MainLoop
from lib.usb import Usb
from lib.action import Action


class RemoteApp:
    usb_active = False
    remote = False

    def __init__(self):
        self.logger = Logger()
        self.main_loop = MainLoop()
        self.usb = Usb()
        self.action = Action()
        Logger.log('Init RemoteApp', True)

    def run(self):
        self.main_loop.set_interval(self.main, .1)

    def find_usb_device(self):
        tty_usb = self.usb.find()
        if tty_usb:
            try:
                success = self.usb.setup(tty_usb)
                if success:
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
            for code in action_codes:
                self.action.run(code)

    def main(self):
        if not self.usb_active:
            self.find_usb_device()
        else:
            self.remote_action()


if __name__ == "__main__":
    app = RemoteApp()
    app.run()
