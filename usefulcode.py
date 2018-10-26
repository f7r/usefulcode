#!/usr/bin/env python3

# 列表去重（保持原有顺序）

def list_dedupe(lst_in):
    from functools import reduce
    func = lambda x,y:x if y in x else x + [y]
    lst_out = reduce(func, [[], ] + lst_in)
    return lst_out

# IP转换为数字

def ip2digitstr(ip):
    import socket, struct
    packedIP = socket.inet_aton(ip)
    digit = struct.unpack("!L", packedIP)[0]
    return str(digit)

# 数字转换为IP

def digitstr2ip(digitstr):
    import socket, struct
    digit = int(digitstr)
    packedIP = struct.pack('!L', digit)
    ip = socket.inet_ntoa(packedIP)
    return ip

# 判断是否为IP

def is_v4_ip(str_ip):
    if '.' not in str_ip:
        return False
    elif str_ip.count('.') != 3:
        return False
    else:
        flag = True
        lst_ip = str_ip.split('.')
        for i in lst_ip:
            try:
                num = int(i)
                if num >=0 and num <= 255:
                    pass
                else:
                    flag = False
            except:
                flag = False
        return flag

# 判断是否为uuid

def is_uuid(str_uuid):
    import re
    r = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    match = re.match(r, str_uuid)
    try:
        if match.string == str_uuid:
            return True
        else:
            return False
    except:
        return False

# 添加字符串输出效果

def printe(string, fcolor, bcolor="", bold=False, 
           underscore=False, blink=False, reverse=False):
    # Print enhanced.
    import sys
    fcolor_code_map = {
                        "black": 30,
                        "red": 31,
                        "green": 32,
                        "yellow": 33,
                        "blue": 34,
                        "magenta": 35,
                        "cyan":36,
                        "white": 37
                      }
    bcolor_code_map = {
                        "black": 40,
                        "red": 41,
                        "green": 42,
                        "yellow": 43,
                        "blue": 44,
                        "magenta": 45,
                        "cyan":46,
                        "white": 47
                      }
    code_list = []
    # Foreground colors.
    if fcolor in fcolor_code_map:
        fcolor_code = fcolor_code_map[fcolor]
        code_list.append(fcolor_code)
    # Background colors
    if bcolor in bcolor_code_map:
        bcolor_code = bcolor_code_map[bcolor]
        code_list.append(bcolor_code)
    # Text attributes
    if bold:
        code_list.append(1)
    if underscore:
        code_list.append(4)
    if blink:
        code_list.append(5)
    if reverse:
        code_list.append(7)
    code = "0"
    for i in code_list:
        code = code + ";" + str(i)
    enhanced_string = "\033[{0}m{1}\033[0m".format(code, string)
    sys.stdout.write(enhanced_string)
    # line break
    print()

# 输出数字进度符

def printpi(percent):
    # Print progress indicator.
    import sys, time
    time.sleep(0.1)
    string = "\033[1000D{0}%\033[0m".format(percent)
    sys.stdout.write(string)
    sys.stdout.flush()
    if percent == 100:
        print()

# 输出进度条

def printpb(percent):
    # Print progress bar.
    import sys, time
    time.sleep(0.1)
    width = int(percent / 4)
    bar = "[" + "#" * width + " " * (25 - width) + "]"
    string = "\033[1000D{0}\033[0m".format(bar)
    sys.stdout.write(string)
    sys.stdout.flush()
    if percent == 100:
        print()

# 得到程序文件运行时的目录

def get_path():
    # Only work in a file.
    import os
    return os.path.dirname(os.path.realpath(__file__))

def get_path():
    from pathlib import Path
    p = Path(__file__)
    s = p.resolve().parent
    return str(s)

# 文件日志示例

import logging
import os
from logging.handlers import RotatingFileHandler

class LogHandler(logging.Logger):

    _fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    _datefmt = "%a, %d %b %Y %H:%M:%S"
    _logpath = "/var/log/pylog"

    def __init__(self, name=None):
        logging.Logger.__init__(self, name)
        self._prepare()
        self.log_file = "{0}/py.log".format(self._logpath)
        formatter = logging.Formatter(self._fmt, self._datefmt)
        rfhandler = RotatingFileHandler(self.log_file, maxBytes=1024*1024, backupCount=5)
        rfhandler.setFormatter(formatter)
        #shandler = logging.StreamHandler()
        #shandler.setFormatter(formatter)
        self.addHandler(rfhandler)
        #self.addHandler(shandler)
        #self.setLevel(logging.INFO)

    def _prepare(self):
        if os.path.exists(self._logpath):
            return
        else:
            os.mkdir(self._logpath)


# 动态定义变量(慎用)
def dynamic_define_vars():
    local_vars = globals()
    VARS = {"a": 1, "b": 2, "c": 3}
    for i in VARS:
        name = "int_" + i
        value = VARS[i]
        local_vars[name] = value


# 设置执行超时
import signal
import time


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                print('start alarm signal.')
                r = func(*args, **kwargs)
                print('close alarm signal.')
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


if __name__ == '__main__':
    def after_timeout():  # 超时后的处理函数
        print("do something after timeout.")

    @set_timeout(2, after_timeout)  # 限时 2 秒
    def connect():  # 要执行的函数
        time.sleep(1)  # 函数执行时间，写大于2的值，可测试超时
        return 'connect success.'

    print(connect())


def run_cmd(cmd):
    import subprocess
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = p.stdout.read()
    return output


# 配置文件
from configparser import SafeConfigParser

class ConfigClass(SafeConfigParser):

    DEFAULT = {}

    def __init__(self, filename):
        super().__init__(self.DEFAULT)
        self.read(filename)


config = ConfigClass("config.ini")
