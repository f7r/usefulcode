# =============================================================================
# Author: falseuser
# Created Time: 2019-01-07 10:12:10
# Last modified: 2019-09-23 12:02:03
# Description: log.py
# =============================================================================
import os
import logging
from logging.handlers import RotatingFileHandler


class SimpleLogger(logging.Logger):

    def __init__(self, name=None):
        logging.Logger.__init__(self, name)
        self._prepare()
        self._add_handlers()

    def get_handlers(self):
        handlers = []
        use_file = True
        use_console = True
        if use_file:
            filename = "/var/log/watcher/{0}.log".format(self.name)
            max_size = 50
            backup_count = 3
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            time_format = "%Y-%m-%d %H:%M:%S"
            level = "DEBUG"
            formatter = logging.Formatter(log_format, time_format)
            file_handler = RotatingFileHandler(
                filename,
                maxBytes=max_size*1024*1024,
                backupCount=backup_count,
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(level.upper())
            handlers.append(file_handler)
        if use_console:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            time_format = "%Y-%m-%d %H:%M:%S"
            level = "INFO"
            formatter = logging.Formatter(log_format, time_format)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(level.upper())
            handlers.append(console_handler)

        return handlers

    def _add_handlers(self):
        enabled_handlers = self.get_handlers()
        for handler_ in enabled_handlers:
            self.addHandler(handler_)

    def _prepare(self):
        self._prepare_dir()

    def _prepare_dir(self):
        use_file = True
        if use_file:
            filename = "/var/log/watcher/{0}.log".format(self.name)
            log_dir = os.path.dirname(filename)
            if os.path.exists(log_dir):
                return
            else:
                os.mkdir(log_dir)
