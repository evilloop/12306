# -*- coding=utf-8 -*-
import sys

PY3 = True if sys.version[0] == '3' else False

if PY3:
    from http import client as httplib
    from http.cookiejar import LWPCookieJar
    from urllib import request as urllib2
else:
    import httplib
    import urllib2
    from cookielib import LWPCookieJar
import ssl
import urllib




cookiejar = LWPCookieJar()
cookiesuppor = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(cookiesuppor, urllib2.HTTPHandler)
urllib2.install_opener(opener)
ssl._create_default_https_context = ssl._create_unverified_context


def get(url):
    try:
        request = urllib2.Request(url=url)
        request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=utf-8")
        request.add_header('X-Requested-With', 'xmlHttpRequest')
        request.add_header('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                           )
        request.add_header('Referer', 'https://kyfw.12306.cn/otn/confirmPassenger/initDc')
        request.add_header('Accept', '*/*')
        result = urllib2.urlopen(request).read()
        assert isinstance(result, object)
        return result
    except httplib.error as e:
        print(e)
        pass
    except urllib2.URLError as e:
        print(e)
        pass
    except urllib2.HTTPBasicAuthHandler as e:
        print(e)
    except urllib2.HTTPError as e:
        print(e)
        pass


def Post(url, data):
    try:
        request = urllib2.Request(url=url, data=urllib.urlencode(data))
        # req.add_header('User-Agent', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0')
        # request = urllib2Post.Request(ajax_url, urllib.urlencode(dc))
        request.add_header("Content-Type", "application/x-www-form-urlencoded;application/json;charset=utf-8")
        request.add_header('X-Requested-With', 'xmlHttpRequest')
        request.add_header('User-Agent', "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                           )
        request.add_header('Referer', 'https://kyfw.12306.cn/otn/confirmPassenger/initDc')
        request.add_header('Accept', '*/*')
        # request.add_header('Accept-Encoding', 'gzip, deflate')
        for i in range(3):
            result = urllib2.urlopen(request).read()
            if result:
                return result
            else:
                print("返回结果为空，正在第{0}重试".format(i))
    except httplib.error as e:
        return e
    except urllib2.URLError as e:
        return e
    except urllib2.HTTPBasicAuthHandler as e:
        print(e)
        return ('error')
    except urllib2.HTTPError as e:
        print(e)
        return ('error')
