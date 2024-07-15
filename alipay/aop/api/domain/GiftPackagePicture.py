#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftPackagePicture(object):

    def __init__(self):
        self._img_index = None
        self._img_url = None

    @property
    def img_index(self):
        return self._img_index

    @img_index.setter
    def img_index(self, value):
        self._img_index = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_index:
            if hasattr(self.img_index, 'to_alipay_dict'):
                params['img_index'] = self.img_index.to_alipay_dict()
            else:
                params['img_index'] = self.img_index
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftPackagePicture()
        if 'img_index' in d:
            o.img_index = d['img_index']
        if 'img_url' in d:
            o.img_url = d['img_url']
        return o


