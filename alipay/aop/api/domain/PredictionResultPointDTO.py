#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PredictionResultPointDTO(object):

    def __init__(self):
        self._forecast_time = None
        self._value = None

    @property
    def forecast_time(self):
        return self._forecast_time

    @forecast_time.setter
    def forecast_time(self, value):
        self._forecast_time = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.forecast_time:
            if hasattr(self.forecast_time, 'to_alipay_dict'):
                params['forecast_time'] = self.forecast_time.to_alipay_dict()
            else:
                params['forecast_time'] = self.forecast_time
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PredictionResultPointDTO()
        if 'forecast_time' in d:
            o.forecast_time = d['forecast_time']
        if 'value' in d:
            o.value = d['value']
        return o


