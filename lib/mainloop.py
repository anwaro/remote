import threading
from lib.threadjob import ThreadJob


class MainLoop:
    def __init__(self):
        self.job = False

    def stop(self):
        if self.job:
            self.job.stop()

    def set_interval(self, fun, delay):
        if self.job:
            self.job.stop()

        event = threading.Event()
        self.job = ThreadJob(fun, event, delay)
        self.job.start()

