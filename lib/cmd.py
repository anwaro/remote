import os
from lib.notify import SysNotify


class Cmd:

    def __init__(self):
        self.notify = SysNotify()

    def run(self, program):
        self.exe(program.get_command())
        self.show_notify(program.get_notify(), icon=program.get_icon())

    @staticmethod
    def exe(command):
        if len(command):
            os.system(command)

    def activate(self, program):
        self.show_notify(program.get_name() + ' activated ', icon=program.get_icon())

    def show_notify(self, title, text='', icon=''):
        if len(title):
            self.notify.send(title, text, file_path_to_icon=icon)
