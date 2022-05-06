#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MaterialUnit(object):

    def __init__(self):
        self._key = None
        self._material = None
        self._play_frequency = None
        self._play_time = None
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
    def play_frequency(self):
        return self._play_frequency

    @play_frequency.setter
    def play_frequency(self, value):
        self._play_frequency = value
    @property
    def play_time(self):
        return self._play_time

    @play_time.setter
    def play_time(self, value):
        self._play_time = value
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
        if self.play_frequency:
            if hasattr(self.play_frequency, 'to_alipay_dict'):
                params['play_frequency'] = self.play_frequency.to_alipay_dict()
            else:
                params['play_frequency'] = self.play_frequency
        if self.play_time:
            if hasattr(self.play_time, 'to_alipay_dict'):
                params['play_time'] = self.play_time.to_alipay_dict()
            else:
                params['play_time'] = self.play_time
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
        if 'play_frequency' in d:
            o.play_frequency = d['play_frequency']
        if 'play_time' in d:
            o.play_time = d['play_time']
        if 'type' in d:
            o.type = d['type']
        return o


