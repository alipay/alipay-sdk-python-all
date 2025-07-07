#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnergyForecastInfo(object):

    def __init__(self):
        self._prediction = None
        self._time = None

    @property
    def prediction(self):
        return self._prediction

    @prediction.setter
    def prediction(self, value):
        self._prediction = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value


    def to_alipay_dict(self):
        params = dict()
        if self.prediction:
            if hasattr(self.prediction, 'to_alipay_dict'):
                params['prediction'] = self.prediction.to_alipay_dict()
            else:
                params['prediction'] = self.prediction
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
        o = EnergyForecastInfo()
        if 'prediction' in d:
            o.prediction = d['prediction']
        if 'time' in d:
            o.time = d['time']
        return o


