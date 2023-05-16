#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ImgFile(object):

    def __init__(self):
        self._img_url = None
        self._img_url_key = None

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def img_url_key(self):
        return self._img_url_key

    @img_url_key.setter
    def img_url_key(self, value):
        self._img_url_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.img_url_key:
            if hasattr(self.img_url_key, 'to_alipay_dict'):
                params['img_url_key'] = self.img_url_key.to_alipay_dict()
            else:
                params['img_url_key'] = self.img_url_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ImgFile()
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'img_url_key' in d:
            o.img_url_key = d['img_url_key']
        return o


