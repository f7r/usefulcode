# =============================================================================
# Author: falseuser
# Created Time: 2019-01-07 10:12:10
# Last modified: 2019-01-09 14:49:51
# Description: log.py
# =============================================================================
import os
import logging
from configparser import SafeConfigParser
from logging.handlers import RotatingFileHandler


class SimpleLogger(logging.Logger):

    def __init__(self, name=None):
        logging.Logger.__init__(self, name)
        self.config = LoggerConfig("config.ini")
        self._prepare()
        self._add_handlers()

    def get_handlers(self):
        handlers = []
        use_file = self.config.getboolean("file", "enable")
        use_console = self.config.getboolean("console", "enable")
        if use_file:
            filename = self.config.get("file", "filename")
            max_size = self.config.getint("file", "max_size")
            backup_count = self.config.get("file", "backup_count")
            log_format = self.config.get("file", "log_format", raw=True)
            time_format = self.config.get("file", "time_format", raw=True)
            level = self.config.get("file", "level")
            formatter = logging.Formatter(log_format, time_format)
            file_handler = RotatingFileHandler(
                filename,
                maxBytes=max_size*1024*1024,
                backupCount=backup_count,
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(level)
            handlers.append(file_handler)
        if use_console:
            log_format = self.config.get("console", "log_format", raw=True)
            time_format = self.config.get("console", "time_format", raw=True)
            level = self.config.get("console", "level")
            formatter = logging.Formatter(log_format, time_format)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(level)
            handlers.append(console_handler)

        return handlers

    def _add_handlers(self):
        enabled_handlers = self.get_handlers()
        for handler_ in enabled_handlers:
            self.addHandler(handler_)

    def _prepare(self):
        self._prepare_dir()

    def _prepare_dir(self):
        use_file = self.config.getboolean("file", "enable")
        if use_file:
            filename = self.config.get("file", "filename")
            log_dir = os.path.dirname(filename)
            if os.path.exists(log_dir):
                return
            else:
                os.mkdir(log_dir)


class LoggerConfig(SafeConfigParser):

    def __init__(self, filename, *args, **kwargs):
        SafeConfigParser.__init__(self, *args, **kwargs)
        self.read(filename)


if __name__ == "__main__":
    logger = SimpleLogger("test")
    logger.info("iiiiii")
    logger.debug("dddddd")
