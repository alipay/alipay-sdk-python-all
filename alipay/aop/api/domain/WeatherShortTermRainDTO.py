#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WeatherShortTermRainDTO(object):

    def __init__(self):
        self._forecast_time = None
        self._precip = None
        self._type = None

    @property
    def forecast_time(self):
        return self._forecast_time

    @forecast_time.setter
    def forecast_time(self, value):
        self._forecast_time = value
    @property
    def precip(self):
        return self._precip

    @precip.setter
    def precip(self, value):
        self._precip = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.forecast_time:
            if hasattr(self.forecast_time, 'to_alipay_dict'):
                params['forecast_time'] = self.forecast_time.to_alipay_dict()
            else:
                params['forecast_time'] = self.forecast_time
        if self.precip:
            if hasattr(self.precip, 'to_alipay_dict'):
                params['precip'] = self.precip.to_alipay_dict()
            else:
                params['precip'] = self.precip
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
        o = WeatherShortTermRainDTO()
        if 'forecast_time' in d:
            o.forecast_time = d['forecast_time']
        if 'precip' in d:
            o.precip = d['precip']
        if 'type' in d:
            o.type = d['type']
        return o


