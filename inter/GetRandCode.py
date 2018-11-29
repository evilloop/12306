# coding=utf-8
import sys

PY3 = True if sys.version[0] == '3' else False

if PY3:
    raw_input = input

from PIL import Image

from config.ticketConf import _get_yaml
from damatuCode.ruokuai import RClient


def getRandCode(is_auto_code, auto_code_type):
    """
    识别验证码
    :return: 坐标
    """
    try:
        if is_auto_code:
            if auto_code_type == 1:
                print(u"打码兔已关闭, 如需使用自动识别，请使用如果平台 auto_code_type == 2")
                return
            if auto_code_type == 2:
                rc = RClient(_get_yaml()["auto_code_account"]["user"], _get_yaml()["auto_code_account"]["pwd"])
                im = open('./tkcode', 'rb').read()
                Result = rc.rk_create(im, 6113)
                if "Result" in Result:
                    return codexy(Ofset=",".join(list(Result["Result"])), is_raw_input=False)
                else:
                    if "Error" in Result and Result["Error"]:
                        print(u"打码平台错误: {0}, 请登录打码平台查看-http://www.ruokuai.com/client/index?6726".format(Result["Error"]))
                        return ""
        else:
            img = Image.open('./tkcode')
            img.show()
            return codexy()
    except:
        pass


def codexy(Ofset=None, is_raw_input=True):
    """
    获取验证码
    :return: str
    """
    if is_raw_input:
        print(u"""
            *****************
            | 1 | 2 | 3 | 4 |
            *****************
            | 5 | 6 | 7 | 8 |
            *****************
            """)
        print(u"验证码分为8个，对应上面数字，例如第一和第二张，输入1, 2")
        Ofset = raw_input(u"输入对应的验证码: ")
    Ofset = Ofset.replace("，", ",")
    select = Ofset.split(',')
    post = []
    offsetsX = 0  # 选择的答案的left值,通过浏览器点击8个小图的中点得到的,这样基本没问题
    offsetsY = 0  # 选择的答案的top值
    for ofset in select:
        if ofset == '1':
            offsetsY = 46
            offsetsX = 42
        elif ofset == '2':
            offsetsY = 46
            offsetsX = 105
        elif ofset == '3':
            offsetsY = 45
            offsetsX = 184
        elif ofset == '4':
            offsetsY = 48
            offsetsX = 256
        elif ofset == '5':
            offsetsY = 36
            offsetsX = 117
        elif ofset == '6':
            offsetsY = 112
            offsetsX = 115
        elif ofset == '7':
            offsetsY = 114
            offsetsX = 181
        elif ofset == '8':
            offsetsY = 111
            offsetsX = 252
        else:
            pass
        post.append(offsetsX)
        post.append(offsetsY)
    randCode = str(post).replace(']', '').replace('[', '').replace("'", '').replace(' ', '')
    print(u"验证码识别坐标为{0}".format(randCode))
    return randCode


def select_codes_to_randcode(select_ids):
    """

    :param select_ids: 1,2,3
    :return:
    """
    select_ids = select_ids.replace("，", ",")
    select = select_ids.split(',')
    post = []
    offsetsX = 0  # 选择的答案的left值,通过浏览器点击8个小图的中点得到的,这样基本没问题
    offsetsY = 0  # 选择的答案的top值
    for ofset in select:
        if ofset == '1':
            offsetsY = 46
            offsetsX = 42
        elif ofset == '2':
            offsetsY = 46
            offsetsX = 105
        elif ofset == '3':
            offsetsY = 45
            offsetsX = 184
        elif ofset == '4':
            offsetsY = 48
            offsetsX = 256
        elif ofset == '5':
            offsetsY = 36
            offsetsX = 117
        elif ofset == '6':
            offsetsY = 112
            offsetsX = 115
        elif ofset == '7':
            offsetsY = 114
            offsetsX = 181
        elif ofset == '8':
            offsetsY = 111
            offsetsX = 252
        else:
            pass
        post.append(offsetsX)
        post.append(offsetsY)
    randCode = str(post).replace(']', '').replace('[', '').replace("'", '').replace(' ', '')
    return randCode
