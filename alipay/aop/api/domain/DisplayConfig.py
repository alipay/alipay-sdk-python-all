#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DisplayConfig(object):

    def __init__(self):
        self._slogan = None
        self._slogan_img = None

    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    @property
    def slogan_img(self):
        return self._slogan_img

    @slogan_img.setter
    def slogan_img(self, value):
        self._slogan_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.slogan:
            if hasattr(self.slogan, 'to_alipay_dict'):
                params['slogan'] = self.slogan.to_alipay_dict()
            else:
                params['slogan'] = self.slogan
        if self.slogan_img:
            if hasattr(self.slogan_img, 'to_alipay_dict'):
                params['slogan_img'] = self.slogan_img.to_alipay_dict()
            else:
                params['slogan_img'] = self.slogan_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DisplayConfig()
        if 'slogan' in d:
            o.slogan = d['slogan']
        if 'slogan_img' in d:
            o.slogan_img = d['slogan_img']
        return o


