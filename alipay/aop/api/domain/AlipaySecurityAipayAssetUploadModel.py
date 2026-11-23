#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityAipayAssetUploadModel(object):

    def __init__(self):
        self._keys = None
        self._scene = None
        self._type = None
        self._values = None

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, value):
        if isinstance(value, list):
            self._keys = list()
            for i in value:
                self._keys.append(i)
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                self._values.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.keys:
            if isinstance(self.keys, list):
                for i in range(0, len(self.keys)):
                    element = self.keys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keys[i] = element.to_alipay_dict()
            if hasattr(self.keys, 'to_alipay_dict'):
                params['keys'] = self.keys.to_alipay_dict()
            else:
                params['keys'] = self.keys
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityAipayAssetUploadModel()
        if 'keys' in d:
            o.keys = d['keys']
        if 'scene' in d:
            o.scene = d['scene']
        if 'type' in d:
            o.type = d['type']
        if 'values' in d:
            o.values = d['values']
        return o


