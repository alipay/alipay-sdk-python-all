#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GiftTemplateBackCoverBox(object):

    def __init__(self):
        self._image_url = None
        self._special_shaped_url = None

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def special_shaped_url(self):
        return self._special_shaped_url

    @special_shaped_url.setter
    def special_shaped_url(self, value):
        self._special_shaped_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.special_shaped_url:
            if hasattr(self.special_shaped_url, 'to_alipay_dict'):
                params['special_shaped_url'] = self.special_shaped_url.to_alipay_dict()
            else:
                params['special_shaped_url'] = self.special_shaped_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GiftTemplateBackCoverBox()
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'special_shaped_url' in d:
            o.special_shaped_url = d['special_shaped_url']
        return o


