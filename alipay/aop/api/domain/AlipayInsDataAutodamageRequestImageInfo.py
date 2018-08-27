#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataAutodamageRequestImageInfo(object):

    def __init__(self):
        self._image_name = None
        self._image_path = None

    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = self.image_name.to_alipay_dict()
            else:
                params['image_name'] = self.image_name
        if self.image_path:
            if hasattr(self.image_path, 'to_alipay_dict'):
                params['image_path'] = self.image_path.to_alipay_dict()
            else:
                params['image_path'] = self.image_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutodamageRequestImageInfo()
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'image_path' in d:
            o.image_path = d['image_path']
        return o


