#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Banner(object):

    def __init__(self):
        self._link = None
        self._picture = None

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, value):
        self._picture = value


    def to_alipay_dict(self):
        params = dict()
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.picture:
            if hasattr(self.picture, 'to_alipay_dict'):
                params['picture'] = self.picture.to_alipay_dict()
            else:
                params['picture'] = self.picture
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Banner()
        if 'link' in d:
            o.link = d['link']
        if 'picture' in d:
            o.picture = d['picture']
        return o


