#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HDFRecordBase(object):

    def __init__(self):
        self._height = None
        self._measure_time = None
        self._weight = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def measure_time(self):
        return self._measure_time

    @measure_time.setter
    def measure_time(self, value):
        self._measure_time = value
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value


    def to_alipay_dict(self):
        params = dict()
        if self.height:
            if hasattr(self.height, 'to_alipay_dict'):
                params['height'] = self.height.to_alipay_dict()
            else:
                params['height'] = self.height
        if self.measure_time:
            if hasattr(self.measure_time, 'to_alipay_dict'):
                params['measure_time'] = self.measure_time.to_alipay_dict()
            else:
                params['measure_time'] = self.measure_time
        if self.weight:
            if hasattr(self.weight, 'to_alipay_dict'):
                params['weight'] = self.weight.to_alipay_dict()
            else:
                params['weight'] = self.weight
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HDFRecordBase()
        if 'height' in d:
            o.height = d['height']
        if 'measure_time' in d:
            o.measure_time = d['measure_time']
        if 'weight' in d:
            o.weight = d['weight']
        return o


