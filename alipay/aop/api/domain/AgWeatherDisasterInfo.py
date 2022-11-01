#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgWeatherDisasterInfo(object):

    def __init__(self):
        self._actual_date = None
        self._addition_info = None
        self._forecast_date = None
        self._high_temperature_index = None
        self._high_temperature_level = None
        self._low_temperature_index = None
        self._low_temperature_level = None
        self._rainstorm_index = None
        self._rainstorm_level = None

    @property
    def actual_date(self):
        return self._actual_date

    @actual_date.setter
    def actual_date(self, value):
        self._actual_date = value
    @property
    def addition_info(self):
        return self._addition_info

    @addition_info.setter
    def addition_info(self, value):
        self._addition_info = value
    @property
    def forecast_date(self):
        return self._forecast_date

    @forecast_date.setter
    def forecast_date(self, value):
        self._forecast_date = value
    @property
    def high_temperature_index(self):
        return self._high_temperature_index

    @high_temperature_index.setter
    def high_temperature_index(self, value):
        self._high_temperature_index = value
    @property
    def high_temperature_level(self):
        return self._high_temperature_level

    @high_temperature_level.setter
    def high_temperature_level(self, value):
        self._high_temperature_level = value
    @property
    def low_temperature_index(self):
        return self._low_temperature_index

    @low_temperature_index.setter
    def low_temperature_index(self, value):
        self._low_temperature_index = value
    @property
    def low_temperature_level(self):
        return self._low_temperature_level

    @low_temperature_level.setter
    def low_temperature_level(self, value):
        self._low_temperature_level = value
    @property
    def rainstorm_index(self):
        return self._rainstorm_index

    @rainstorm_index.setter
    def rainstorm_index(self, value):
        self._rainstorm_index = value
    @property
    def rainstorm_level(self):
        return self._rainstorm_level

    @rainstorm_level.setter
    def rainstorm_level(self, value):
        self._rainstorm_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_date:
            if hasattr(self.actual_date, 'to_alipay_dict'):
                params['actual_date'] = self.actual_date.to_alipay_dict()
            else:
                params['actual_date'] = self.actual_date
        if self.addition_info:
            if hasattr(self.addition_info, 'to_alipay_dict'):
                params['addition_info'] = self.addition_info.to_alipay_dict()
            else:
                params['addition_info'] = self.addition_info
        if self.forecast_date:
            if hasattr(self.forecast_date, 'to_alipay_dict'):
                params['forecast_date'] = self.forecast_date.to_alipay_dict()
            else:
                params['forecast_date'] = self.forecast_date
        if self.high_temperature_index:
            if hasattr(self.high_temperature_index, 'to_alipay_dict'):
                params['high_temperature_index'] = self.high_temperature_index.to_alipay_dict()
            else:
                params['high_temperature_index'] = self.high_temperature_index
        if self.high_temperature_level:
            if hasattr(self.high_temperature_level, 'to_alipay_dict'):
                params['high_temperature_level'] = self.high_temperature_level.to_alipay_dict()
            else:
                params['high_temperature_level'] = self.high_temperature_level
        if self.low_temperature_index:
            if hasattr(self.low_temperature_index, 'to_alipay_dict'):
                params['low_temperature_index'] = self.low_temperature_index.to_alipay_dict()
            else:
                params['low_temperature_index'] = self.low_temperature_index
        if self.low_temperature_level:
            if hasattr(self.low_temperature_level, 'to_alipay_dict'):
                params['low_temperature_level'] = self.low_temperature_level.to_alipay_dict()
            else:
                params['low_temperature_level'] = self.low_temperature_level
        if self.rainstorm_index:
            if hasattr(self.rainstorm_index, 'to_alipay_dict'):
                params['rainstorm_index'] = self.rainstorm_index.to_alipay_dict()
            else:
                params['rainstorm_index'] = self.rainstorm_index
        if self.rainstorm_level:
            if hasattr(self.rainstorm_level, 'to_alipay_dict'):
                params['rainstorm_level'] = self.rainstorm_level.to_alipay_dict()
            else:
                params['rainstorm_level'] = self.rainstorm_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgWeatherDisasterInfo()
        if 'actual_date' in d:
            o.actual_date = d['actual_date']
        if 'addition_info' in d:
            o.addition_info = d['addition_info']
        if 'forecast_date' in d:
            o.forecast_date = d['forecast_date']
        if 'high_temperature_index' in d:
            o.high_temperature_index = d['high_temperature_index']
        if 'high_temperature_level' in d:
            o.high_temperature_level = d['high_temperature_level']
        if 'low_temperature_index' in d:
            o.low_temperature_index = d['low_temperature_index']
        if 'low_temperature_level' in d:
            o.low_temperature_level = d['low_temperature_level']
        if 'rainstorm_index' in d:
            o.rainstorm_index = d['rainstorm_index']
        if 'rainstorm_level' in d:
            o.rainstorm_level = d['rainstorm_level']
        return o


