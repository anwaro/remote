import os


class Cmd:
    program_name = ''

    def __init__(self):
        pass

    def get_all_commands(self):
        return {}

    def get_command(self, index):
        cmd = self.get_all_commands()
        if index in cmd:
            return cmd[index]
        return {'command': ''}

    def run(self, index):
        data = self.get_command(index)
        self.exe(data['command'])
        if 'notify' in data:
            self.notify(data['notify'])

    def exe(self, command):
        if len(command):
            os.system(command)

    def activate(self):
        self.notify(self.program_name + ' activated')

    def notify(self, text):
        print(text)
