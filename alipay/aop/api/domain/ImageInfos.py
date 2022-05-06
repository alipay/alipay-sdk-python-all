#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ImageInfos(object):

    def __init__(self):
        self._image = None
        self._image_type = None
        self._md_5 = None
        self._name = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value
    @property
    def md_5(self):
        return self._md_5

    @md_5.setter
    def md_5(self, value):
        self._md_5 = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
        if self.md_5:
            if hasattr(self.md_5, 'to_alipay_dict'):
                params['md_5'] = self.md_5.to_alipay_dict()
            else:
                params['md_5'] = self.md_5
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ImageInfos()
        if 'image' in d:
            o.image = d['image']
        if 'image_type' in d:
            o.image_type = d['image_type']
        if 'md_5' in d:
            o.md_5 = d['md_5']
        if 'name' in d:
            o.name = d['name']
        return o


