#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCognitiveOcrVehiclelicenseQueryModel(object):

    def __init__(self):
        self._image_content = None
        self._side = None

    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value
    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value


    def to_alipay_dict(self):
        params = dict()
        if self.image_content:
            if hasattr(self.image_content, 'to_alipay_dict'):
                params['image_content'] = self.image_content.to_alipay_dict()
            else:
                params['image_content'] = self.image_content
        if self.side:
            if hasattr(self.side, 'to_alipay_dict'):
                params['side'] = self.side.to_alipay_dict()
            else:
                params['side'] = self.side
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCognitiveOcrVehiclelicenseQueryModel()
        if 'image_content' in d:
            o.image_content = d['image_content']
        if 'side' in d:
            o.side = d['side']
        return o


