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
