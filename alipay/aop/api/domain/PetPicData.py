#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PetPicData(object):

    def __init__(self):
        self._image_type = None
        self._image_url = None

    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PetPicData()
        if 'image_type' in d:
            o.image_type = d['image_type']
        if 'image_url' in d:
            o.image_url = d['image_url']
        return o


