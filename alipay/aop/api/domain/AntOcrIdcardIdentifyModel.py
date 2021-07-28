#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntOcrIdcardIdentifyModel(object):

    def __init__(self):
        self._image = None
        self._side = None
        self._type = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.side:
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = self.side.to_alipay_dict()
            else:
                params['side'] = self.side
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntOcrIdcardIdentifyModel()
        if 'image' in d:
            o.image = d['image']
        if 'side' in d:
            o.side = d['side']
        if 'type' in d:
            o.type = d['type']
        return o


