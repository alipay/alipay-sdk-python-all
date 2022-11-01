#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Fence import Fence


class HeatMapData(object):

    def __init__(self):
        self._city_code = None
        self._end_time = None
        self._fences = None
        self._start_time = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fences(self):
        return self._fences

    @fences.setter
    def fences(self, value):
        if isinstance(value, list):
            self._fences = list()
            for i in value:
                if isinstance(i, Fence):
                    self._fences.append(i)
                else:
                    self._fences.append(Fence.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.fences:
            if isinstance(self.fences, list):
                for i in range(0, len(self.fences)):
                    element = self.fences[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fences[i] = element.to_alipay_dict()
            if hasattr(self.fences, 'to_alipay_dict'):
                params['fences'] = self.fences.to_alipay_dict()
            else:
                params['fences'] = self.fences
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HeatMapData()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'fences' in d:
            o.fences = d['fences']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


