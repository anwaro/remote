from lib.threadjob import ThreadJob


class MainLoop:
    def __init__(self):
        self.job = None

    def set_interval(self, fun, delay):
        if self.job:
            self.job.stop()
        self.job = ThreadJob(fun, delay)
        self.job.start()

    def stop(self):
        if self.job:
            self.job.stop()

