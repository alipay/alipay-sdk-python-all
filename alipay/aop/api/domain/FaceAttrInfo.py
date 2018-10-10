#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FaceAttrInfo(object):

    def __init__(self):
        self._rect = None

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value


    def to_alipay_dict(self):
        params = dict()
        if self.rect:
            if hasattr(self.rect, 'to_alipay_dict'):
                params['rect'] = self.rect.to_alipay_dict()
            else:
                params['rect'] = self.rect
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FaceAttrInfo()
        if 'rect' in d:
            o.rect = d['rect']
        return o


