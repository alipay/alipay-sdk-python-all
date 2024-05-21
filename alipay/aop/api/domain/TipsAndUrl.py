#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TipsAndUrl(object):

    def __init__(self):
        self._tips = None
        self._url = None

    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TipsAndUrl()
        if 'tips' in d:
            o.tips = d['tips']
        if 'url' in d:
            o.url = d['url']
        return o


