# coding=utf-8
import copy
import random
import time
from PIL import Image
import os

base_dir = os.path.dirname(os.path.dirname(__file__))

pic_dir = os.path.join(base_dir, 'tmp', 'pic')


def getPassCodeNewOrderAndLogin(session, imgType):
    """
    下载验证码
    :param session:
    :param imgType: 下载验证码类型，login=登录验证码，其余为订单验证码
    :return:
    """
    if imgType == "login":
        codeImgUrl = copy.deepcopy(session.urls["getCodeImg"])
        codeImgUrl["req_url"] = codeImgUrl["req_url"].format(random.random())
    else:
        codeImgUrl = copy.deepcopy(session.urls["codeImgByOrder"])
        codeImgUrl["req_url"] = codeImgUrl["req_url"].format(random.random())
    print (u"下载验证码...")
    img_path = './tkcode.png'
    result = session.httpClint.send(codeImgUrl)
    try:
        if isinstance(result, dict):
            print(u"下载验证码失败, 请手动检查是否ip被封，或者重试，请求地址：{}".format(codeImgUrl))
            return False
        else:
            print(u"下载验证码成功")
            open(img_path, 'wb').write(result)
            # 裁图
            im = Image.open(img_path)
            print(im.size)
            top_x = 0
            top_y = 0
            top_w = im.size[0]
            top_h = 41
            top_im = im.crop((top_x, top_y, top_w, top_h))
            top_im.save(os.path.join(pic_dir, 'top.png'))
            left_border_size = 3
            pic_size = (im.size[0]-2)//4
            for i in range(8):
                if i <= 3:
                    pic_x = left_border_size + pic_size*i
                    pic_y = top_h
                else:
                    pic_x = left_border_size + pic_size*(i-4)
                    pic_y = top_h + pic_size
                pic_w = pic_size
                pic_h = pic_size
                offset_x = pic_x + pic_w
                offset_y = pic_y + pic_h
                print((pic_x, pic_y, pic_w, pic_h), (offset_x, offset_y))
                opt_im = im.crop((pic_x, pic_y, pic_x+pic_w, pic_y+pic_h))
                opt_im.save(os.path.join(pic_dir, './%d.png' % i))
            im.close()
            return True
    except OSError:
        print (u"验证码下载失败，可能ip被封，确认请手动请求: {0}".format(codeImgUrl))


# if __name__ == '__main__':
#     pic = '/Users/roc.maple/work/12306/tkcode.png'
#     # 裁图
#     im = Image.open(pic)
#     print(im.size)
#     top_x = 0
#     top_y = 0
#     top_w = im.size[0]
#     top_h = 40
#     top_im = im.crop((top_x, top_y, top_w, top_h))
#     top_im.save('./top.png')
#     left_border_size = 3
#     pic_size = (im.size[0]-2) // 4
#     for i in range(8):
#         if i <= 3:
#             pic_x = left_border_size + pic_size * i
#             pic_y = top_h
#         else:
#             pic_x = left_border_size + pic_size * (i - 4)
#             pic_y = top_h + pic_size
#         pic_w = pic_size
#         pic_h = pic_size
#         offset_x = pic_x + pic_w
#         offset_y = pic_y + pic_h
#         print((pic_x, pic_y, pic_w, pic_h), (offset_x, offset_y))
#         opt_im = im.crop((pic_x, pic_y, pic_x + pic_w, pic_y + pic_h))
#         opt_im.save('./%d.png' % i)
