#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WaybillStep(object):

    def __init__(self):
        self._city = None
        self._desc = None
        self._time = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WaybillStep()
        if 'city' in d:
            o.city = d['city']
        if 'desc' in d:
            o.desc = d['desc']
        if 'time' in d:
            o.time = d['time']
        return o


