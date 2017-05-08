from logging import StreamHandler, Formatter
import sys
import os


class LogHandler(StreamHandler):

    def __init__(self):
        type = os.getenv('LOGGING_TYPE') or sys.stdout
        StreamHandler.__init__(self, type)
        format = "%(asctime)s [%(threadName)10s][%(module)10s][%(lineno)4s][%(levelname)8s] %(message)s"
        format_date = '%Y-%m-%dT%H:%M:%S%Z'
        formatter = Formatter(format, format_date)
        self.setFormatter(formatter)