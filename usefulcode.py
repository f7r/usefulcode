#!/usr/bin/env python3

# 列表去重（保持原有顺序）

def list_dedupe(lst_in):
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
    code_list = []
    # Foreground colors.
    if fcolor == "black":
        code_list.append(30)
    elif fcolor == "red":
        code_list.append(31)
    elif f_color == "green":
        code_list.append(32)
    elif fcolor == "yellow":
        code_list.append(33)
    elif fcolor == "blue":
        code_list.append(34)
    elif fcolor == "magenta":
        code_list.append(35)
    elif fcolor == "cyan":
        code_list.append(36)
    elif fcolor == "white":
        code_list.append(37)
    # Background colors
    if bcolor == "black":
        code_list.append(40)
    elif bcolor == "red":
        code_list.append(41)
    elif bcolor == "green":
        code_list.append(42)
    elif bcolor == "yellow":
        code_list.append(43)
    elif bcolor == "blue":
        code_list.append(44)
    elif bcolor == "magenta":
        code_list.append(45)
    elif bcolor == "cyan":
        code_list.append(46)
    elif bcolor == "white":
        code_list.append(47)
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
    color_string = "\033[{0}m{1}\033[0m".format(code, string)
    sys.stdout.write(color_string)
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
