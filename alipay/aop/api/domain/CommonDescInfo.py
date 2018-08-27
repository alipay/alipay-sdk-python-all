#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommonDescInfo(object):

    def __init__(self):
        self._img = None
        self._text = None

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, value):
        self._img = value
    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value


    def to_alipay_dict(self):
        params = dict()
        if self.img:
            if hasattr(self.img, 'to_alipay_dict'):
                params['img'] = self.img.to_alipay_dict()
            else:
                params['img'] = self.img
        if self.text:
            if hasattr(self.text, 'to_alipay_dict'):
                params['text'] = self.text.to_alipay_dict()
            else:
                params['text'] = self.text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommonDescInfo()
        if 'img' in d:
            o.img = d['img']
        if 'text' in d:
            o.text = d['text']
        return o


