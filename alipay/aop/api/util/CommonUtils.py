# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
from alipay.aop.api.constant.CommonConstants import PYTHON_VERSION_3


def has_value(m, key):
    if not m:
        return False
    if not (key in m):
        return False
    if not m[key]:
        return False
    return True


def get_file_suffix(bs):
    if not bs or len(bs) < 10:
      return None
    if PYTHON_VERSION_3:
        if bs[0] == 71 and bs[1] == 73 and bs[2] == 70:
            return "GIF"
        if bs[1] == 80 and bs[2] == 78 and bs[3] == 71:
            return "PNG"
        if bs[6] == 74 and bs[7] == 70 and bs[8] == 73 and bs[9] == 70:
            return "JPG"
        if bs[0] == 66 and bs[1] == 77:
            return "BMP"
    else:
        if ord(bs[0]) == 71 and ord(bs[1]) == 73 and ord(bs[2]) == 70:
          return "GIF"
        if ord(bs[1]) == 80 and ord(bs[2]) == 78 and ord(bs[3]) == 71:
          return "PNG"
        if ord(bs[6]) == 74 and ord(bs[7]) == 70 and ord(bs[8]) == 73 and ord(bs[9]) == 70:
          return "JPG"
        if ord(bs[0]) == 66 and ord(bs[1]) == 77:
          return "BMP"
    return None


def get_mime_type(bs):
    suffix = get_file_suffix(bs)
    mime_type = "application/octet-stream"
    if suffix == "JPG":
        mime_type = "image/jpeg"
    elif suffix == "GIF":
        mime_type = "image/gif"
    elif suffix == "PNG":
        mime_type = "image/png"
    elif suffix == "BMP":
        mime_type = "image/bmp"
    return mime_type

