#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkuPropsDetail(object):

    def __init__(self):
        self._image = None
        self._name = None
        self._vid = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value


    def to_alipay_dict(self):
        params = dict()
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.vid:
            if hasattr(self.vid, 'to_alipay_dict'):
                params['vid'] = self.vid.to_alipay_dict()
            else:
                params['vid'] = self.vid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkuPropsDetail()
        if 'image' in d:
            o.image = d['image']
        if 'name' in d:
            o.name = d['name']
        if 'vid' in d:
            o.vid = d['vid']
        return o


