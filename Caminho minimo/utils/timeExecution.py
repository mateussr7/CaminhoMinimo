class TimeExecution:

    def __init__(self, init_time):
        self.init_time = init_time
        self.finish_time = 0

    def set_finish_time(self, finish_time):
        self.finish_time = finish_time

    def calc_execution_time(self):
        return self.finish_time - self.init_time
