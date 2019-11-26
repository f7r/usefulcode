# =============================================================================
# Author: falseuser
# Created Time: 2019-09-19 13:29:35
# Last modified: 2019-09-26 14:08:16
# Description: watcher_1.py
# =============================================================================
import json
import guazi
import youxin
import renrenche
import che168
import directmail
from log import SimpleLogger


TOADDRESS = ""
ACCOUNT_NAME = ""
ACCESS_KEY_ID = ""
ACCESS_KEY_SECRET = ""
logger = SimpleLogger("cars")


def match(keyword, cars):
    matched = []
    for car in cars:
        title = car[0]
        if keyword in title:
            matched.append(car)
    return matched


def get_notify_body(cars):
    global notified
    p = ""
    html_body_base = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>汽车列表</title>
    </head>
    <body>
        <h1>符合要求的汽车列表</h1>
        {p}
    </body>
    </html>
    """
    html_body_base = html_body_base.replace("\n    ", "\n")
    notify_list = []
    for car in cars:
        href = car[1]
        if href not in notified:
            notify_list.append(car)
    i = 1
    for car in notify_list:
        p += "<p>{0}   <a href=\"{1}\">{1}</a></p>\n    ".format(i, car[1])
        notified.add(car[1])
        i += 1
    main_body = html_body_base.format(p=p)

    backup_body = """
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Found {0} results</h1>
    </body>
    </html>
    """.format(len(notify_list))

    msg = (
        "Should notify {0} results to {1}"
    ).format(len(notify_list), TOADDRESS)
    logger.info(msg)
    if len(notify_list) > 0:
        do = True
    else:
        do = False
    return do, main_body, backup_body


def notify(cars):
    global notified
    try:
        with open("notified.json") as f:
            notified_list = json.load(f)
    except OSError:
        notified_list = []
    notified = set(notified_list)
    do, main_body, backup_body = get_notify_body(cars)

    def sendmail(body):
        print(body)
        # TODO
        with open("notified.json", "w") as f:
            notified_list = list(notified)
            json.dump(notified_list, f)

    try:
        if do:
            sendmail(main_body)
            logger.info("Send success")
    except directmail.RequestError as e:
        logger.exception(e)
    except directmail.SendMailError as e:
        if str(e) == "InvalidSendMail.Spam":
            sendmail(backup_body)


def main():
    urls = {
        "guazi_brz": "https://www.guazi.com/www/subaru-brz/c-1n1/",
        "guazi_86": "https://www.guazi.com/www/86/c-1n1/",
        "youxin_brz": "https://www.xin.com/chongqing/sibalu/brz/sn_g2/",
        "youxin_86": "https://www.xin.com/chongqing/fengtian/86/sn_g2/",
        "renrenche_brz": "https://www.renrenche.com/cn/sibalu_sibaluBRZ/ge-s/",
        "renrenche_86": (
            "https://www.renrenche.com/cn/fengtian_fengtian86/ge-s/"
        ),
        "che168_brz": (
            "https://www.che168.com/china/sibalu/sibalubrz"
            "/a0_0msdg1scncgpi1ltocsp1ex/"
        ),
        "che168_86": (
            "https://www.che168.com/china/fengtian/fengtian86"
            "/a0_0msdg1scncgpi1ltocsp1ex/"
        ),
    }
    all_matched = []
    all_brz = []
    all_86 = []

    # BRZ  2017/2020
    all_brz.extend(guazi.get_cars(urls['guazi_brz']))
    all_brz.extend(youxin.get_cars(urls['youxin_brz']))
    all_brz.extend(renrenche.get_cars(urls['renrenche_brz']))
    all_brz.extend(che168.get_cars(urls['che168_brz']))

    matched = match("2020", all_brz)
    all_matched.extend(matched)

    # 86  2017/2019
    all_86.extend(guazi.get_cars(urls['guazi_86']))
    all_86.extend(youxin.get_cars(urls['youxin_86']))
    all_86.extend(renrenche.get_cars(urls['renrenche_86']))
    all_86.extend(che168.get_cars(urls['che168_86']))

    matched = match("2019", all_86)
    all_matched.extend(matched)

    if len(all_matched) > 0:
        #notify(all_matched)
        print(all_matched)
    else:
        logger.info("No Matched")


if __name__ == "__main__":
    main()
