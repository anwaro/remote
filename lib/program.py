from lib.helper import Helper


class Program:
    index = 0
    name = ''
    icon = ''
    key = {}

    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def set_index(self, index):
        self.index = index
        return self

    def get_name(self):
        return self.name

    def get_icon(self):
        if len(self.icon):
            return Helper.app_path() + "/icon/" + self.icon
        return ''

    def get_item(self):
        return self.get(self.key, self.index, False)

    def get_command(self):
        return self.get(self.get_item(), 'cmd', '')

    def get_notify(self):
        return self.get(self.get_item(), 'notify', '')

    @staticmethod
    def get(obj, key, default):
        if obj and key in obj:
            return obj[key]
        return default

