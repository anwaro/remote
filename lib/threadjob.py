import threading


class ThreadJob(threading.Thread):
    def __init__(self, callback, interval):
        """
        runs the callback function after interval seconds

        :param self
        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: fun
        :type interval: int
        """
        self.callback = callback
        self.event = threading.Event()
        self.interval = interval
        self.active = True
        super(ThreadJob, self).__init__()

    def run(self):
        while not self.event.wait(self.interval) and self.active:
            self.callback()

    def stop(self):
        self.active = False
