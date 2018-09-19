#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdvertItem(object):

    def __init__(self):
        self._img_url = None
        self._link_url = None

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def link_url(self):
        return self._link_url

    @link_url.setter
    def link_url(self, value):
        self._link_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.link_url:
            if hasattr(self.link_url, 'to_alipay_dict'):
                params['link_url'] = self.link_url.to_alipay_dict()
            else:
                params['link_url'] = self.link_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdvertItem()
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'link_url' in d:
            o.link_url = d['link_url']
        return o


