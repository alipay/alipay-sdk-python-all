#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgWeatherWeeklyStats(object):

    def __init__(self):
        self._acc_precipitation = None
        self._acc_temperature = None
        self._create_date = None
        self._update_date = None

    @property
    def acc_precipitation(self):
        return self._acc_precipitation

    @acc_precipitation.setter
    def acc_precipitation(self, value):
        self._acc_precipitation = value
    @property
    def acc_temperature(self):
        return self._acc_temperature

    @acc_temperature.setter
    def acc_temperature(self, value):
        self._acc_temperature = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.acc_precipitation:
            if hasattr(self.acc_precipitation, 'to_alipay_dict'):
                params['acc_precipitation'] = self.acc_precipitation.to_alipay_dict()
            else:
                params['acc_precipitation'] = self.acc_precipitation
        if self.acc_temperature:
            if hasattr(self.acc_temperature, 'to_alipay_dict'):
                params['acc_temperature'] = self.acc_temperature.to_alipay_dict()
            else:
                params['acc_temperature'] = self.acc_temperature
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.update_date:
            if hasattr(self.update_date, 'to_alipay_dict'):
                params['update_date'] = self.update_date.to_alipay_dict()
            else:
                params['update_date'] = self.update_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AgWeatherWeeklyStats()
        if 'acc_precipitation' in d:
            o.acc_precipitation = d['acc_precipitation']
        if 'acc_temperature' in d:
            o.acc_temperature = d['acc_temperature']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'update_date' in d:
            o.update_date = d['update_date']
        return o


