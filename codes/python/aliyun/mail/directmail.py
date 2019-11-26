# =============================================================================
# Author: falseuser
# Created Time: 2019-09-18 14:02:20
# Last modified: 2019-09-18 17:51:41
# Description: directmail.py Aliyun 邮件推送
# Reference: https://help.aliyun.com/document_detail/29434.html
# =============================================================================
import uuid
import hmac
import base64
import datetime
from urllib.parse import urlencode, quote
from collections import OrderedDict
import requests


API_HOST = "dm.aliyuncs.com"
REGION_ID = "cn-hangzhou"
VERSION = "2015-11-23"


def get_public_parameters(access_key_id):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    parameters = {
        "Format": "json",
        "Version": VERSION,
        "AccessKeyId": access_key_id,
        "SignatureMethod": "HMAC-SHA1",
        "Timestamp": timestamp,
        "SignatureVersion": "1.0",
        "SignatureNonce": str(uuid.uuid4()),
        "RegionId": REGION_ID,
    }
    return parameters


def get_signature(parameters, access_key_secret):
    ordered_parameters = OrderedDict()
    keys = sorted(parameters.keys())
    for key in keys:
        ordered_parameters[key] = parameters[key]
    encoded_parameters = urlencode(ordered_parameters)
    encoded_parameters = encoded_parameters.replace('+', '%20')
    encoded_parameters = encoded_parameters.replace('*', '%2A')
    encoded_parameters = encoded_parameters.replace('%7E', '~')
    string_to_sign = (
        "POST" + "&" + quote("/", safe="") + "&" +
        quote(encoded_parameters)
    )
    key = access_key_secret + "&"
    h = hmac.new(key.encode(), string_to_sign.encode(), digestmod='sha1')
    return base64.b64encode(h.digest())


def send_mail_single(account_name, access_key_id, access_key_secret, message):
    url = "https://" + API_HOST
    parameters = {
        "Action": "SingleSendMail",
        "AccountName": account_name,
        "ReplyToAddress": False,
        "AddressType": 1,
        "ToAddress": message.get("ToAddress"),
        "FromAlias": message.get("FromAlias"),
        "Subject": message.get("Subject"),
        "TagName": "auto",
        # "HtmlBody": "",
        "TextBody": message.get("TextBody"),
        "ClickTrace": 0,
    }
    public_parameters = get_public_parameters(access_key_id)
    parameters.update(public_parameters)
    signature = get_signature(parameters, access_key_secret)
    parameters['Signature'] = signature
    try:
        r = requests.post(url, data=parameters)
    except Exception as e:
        print(e)
    else:
        if r.status_code == 200:
            return
        else:
            print(r.status_code)
            res = r.json()
            print(res.get('Code'))
