import gi
gi.require_version('Notify', '0.7')
from gi.repository import GObject, Notify


class SysNotify(GObject.Object):
    def __init__(self):
        super(SysNotify, self).__init__()
        Notify.init("Remote")
        self.notify = Notify.Notification.new("", "")

    def send(self, title, text, file_path_to_icon=""):
        self.notify.update(title, text, file_path_to_icon)
        self.notify.show()
