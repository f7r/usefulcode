# =============================================================================
# Author: falseuser
# Created Time: 2019-01-07 10:12:10
# Last modified: 2019-03-15 15:00:10
# Description: log.py
# =============================================================================
import os
import time
import logging
import functools
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
            file_handler.setLevel(level.upper())
            handlers.append(file_handler)
        if use_console:
            log_format = self.config.get("console", "log_format", raw=True)
            time_format = self.config.get("console", "time_format", raw=True)
            level = self.config.get("console", "level")
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


class ComplexLogger(logging.Logger):

    LOG_FILENAME = "/var/log/ucwi-mgr/complex.log"
    LOG_FORMAT = (
        "%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s - %(message)s"
    )
    LOG_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        logging.Logger.__init__(self, "complex")
        self._prepare_dir()
        self._add_handler()

    def _add_handler(self):
        formatter = logging.Formatter(
            self.LOG_FORMAT,
            self.LOG_TIME_FORMAT,
        )
        file_handler = RotatingFileHandler(
            LOG_FILENAME,
            maxBytes=200 * 1024 * 1024,
            backupCount=5,
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        self.addHandler(file_handler)

    def _prepare_dir(self):
        use_file = True
        if use_file:
            log_dir = os.path.dirname(LOG_FILENAME)
            if os.path.exists(log_dir):
                return
            else:
                os.mkdir(log_dir)


class ComplexLoggerDecorator(object):

    def __init__(self):
        self.logger = ComplexLogger()
        self.on = True

    def __call__(self, func):
        if self.on:
            return self.start_log(func)
        else:
            return func

    def start_log(self, func):
        @functools.wraps(func)
        def logged(*args, **kwargs):
            t0 = time.time()
            result = func(*args, **kwargs)
            used_time = time.time() - t0
            func_name = func.__name__
            msg = (
                "\n\t" "Funcation name: {0}"
                "\n\t" "Runed time: {1:.4f}"
                "\n\t" "args: {2}, kwargs: {3}"
                "\n\t" "returned result: {4}"
            ).format(func_name, used_time, args, kwargs, result)
            self.logger.debug(msg)
            return result
        return logged


if __name__ == "__main__":
    logger = SimpleLogger("test")
    logger.info("iiiiii")
    logger.debug("dddddd")
