#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaterialUnit(object):

    def __init__(self):
        self._key = None
        self._material = None
        self._type = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.material:
            if hasattr(self.material, 'to_alipay_dict'):
                params['material'] = self.material.to_alipay_dict()
            else:
                params['material'] = self.material
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
        o = MaterialUnit()
        if 'key' in d:
            o.key = d['key']
        if 'material' in d:
            o.material = d['material']
        if 'type' in d:
            o.type = d['type']
        return o


