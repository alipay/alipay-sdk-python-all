#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrISVImageDTO(object):

    def __init__(self):
        self._image_format = None
        self._image_id = None
        self._image_type = None

    @property
    def image_format(self):
        return self._image_format

    @image_format.setter
    def image_format(self, value):
        self._image_format = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_format:
            if hasattr(self.image_format, 'to_alipay_dict'):
                params['image_format'] = self.image_format.to_alipay_dict()
            else:
                params['image_format'] = self.image_format
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVImageDTO()
        if 'image_format' in d:
            o.image_format = d['image_format']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'image_type' in d:
            o.image_type = d['image_type']
        return o


