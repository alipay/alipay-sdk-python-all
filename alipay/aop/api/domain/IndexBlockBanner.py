#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndexBlockBanner(object):

    def __init__(self):
        self._image_url = None
        self._jump_url = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndexBlockBanner()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        return o


