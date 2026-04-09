#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VenueConfigModel(object):

    def __init__(self):
        self._max_capacity = None
        self._min_stay_minutes = None

    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        self._max_capacity = value
    @property
    def min_stay_minutes(self):
        return self._min_stay_minutes

    @min_stay_minutes.setter
    def min_stay_minutes(self, value):
        self._min_stay_minutes = value


    def to_alipay_dict(self):
        params = dict()
        if self.max_capacity:
            if hasattr(self.max_capacity, 'to_alipay_dict'):
                params['max_capacity'] = self.max_capacity.to_alipay_dict()
            else:
                params['max_capacity'] = self.max_capacity
        if self.min_stay_minutes:
            if hasattr(self.min_stay_minutes, 'to_alipay_dict'):
                params['min_stay_minutes'] = self.min_stay_minutes.to_alipay_dict()
            else:
                params['min_stay_minutes'] = self.min_stay_minutes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VenueConfigModel()
        if 'max_capacity' in d:
            o.max_capacity = d['max_capacity']
        if 'min_stay_minutes' in d:
            o.min_stay_minutes = d['min_stay_minutes']
        return o


