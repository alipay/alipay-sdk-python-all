#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AgWeatherDisasterHistory(object):

    def __init__(self):
        self._create_date = None
        self._high_temperature_days = None
        self._high_temperature_level = None
        self._low_temperature_days = None
        self._low_temperature_level = None
        self._rainstorm_days = None
        self._rainstorm_level = None
        self._update_date = None

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def high_temperature_days(self):
        return self._high_temperature_days

    @high_temperature_days.setter
    def high_temperature_days(self, value):
        self._high_temperature_days = value
    @property
    def high_temperature_level(self):
        return self._high_temperature_level

    @high_temperature_level.setter
    def high_temperature_level(self, value):
        self._high_temperature_level = value
    @property
    def low_temperature_days(self):
        return self._low_temperature_days

    @low_temperature_days.setter
    def low_temperature_days(self, value):
        self._low_temperature_days = value
    @property
    def low_temperature_level(self):
        return self._low_temperature_level

    @low_temperature_level.setter
    def low_temperature_level(self, value):
        self._low_temperature_level = value
    @property
    def rainstorm_days(self):
        return self._rainstorm_days

    @rainstorm_days.setter
    def rainstorm_days(self, value):
        self._rainstorm_days = value
    @property
    def rainstorm_level(self):
        return self._rainstorm_level

    @rainstorm_level.setter
    def rainstorm_level(self, value):
        self._rainstorm_level = value
    @property
    def update_date(self):
        return self._update_date

    @update_date.setter
    def update_date(self, value):
        self._update_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.high_temperature_days:
            if hasattr(self.high_temperature_days, 'to_alipay_dict'):
                params['high_temperature_days'] = self.high_temperature_days.to_alipay_dict()
            else:
                params['high_temperature_days'] = self.high_temperature_days
        if self.high_temperature_level:
            if hasattr(self.high_temperature_level, 'to_alipay_dict'):
                params['high_temperature_level'] = self.high_temperature_level.to_alipay_dict()
            else:
                params['high_temperature_level'] = self.high_temperature_level
        if self.low_temperature_days:
            if hasattr(self.low_temperature_days, 'to_alipay_dict'):
                params['low_temperature_days'] = self.low_temperature_days.to_alipay_dict()
            else:
                params['low_temperature_days'] = self.low_temperature_days
        if self.low_temperature_level:
            if hasattr(self.low_temperature_level, 'to_alipay_dict'):
                params['low_temperature_level'] = self.low_temperature_level.to_alipay_dict()
            else:
                params['low_temperature_level'] = self.low_temperature_level
        if self.rainstorm_days:
            if hasattr(self.rainstorm_days, 'to_alipay_dict'):
                params['rainstorm_days'] = self.rainstorm_days.to_alipay_dict()
            else:
                params['rainstorm_days'] = self.rainstorm_days
        if self.rainstorm_level:
            if hasattr(self.rainstorm_level, 'to_alipay_dict'):
                params['rainstorm_level'] = self.rainstorm_level.to_alipay_dict()
            else:
                params['rainstorm_level'] = self.rainstorm_level
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
        o = AgWeatherDisasterHistory()
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'high_temperature_days' in d:
            o.high_temperature_days = d['high_temperature_days']
        if 'high_temperature_level' in d:
            o.high_temperature_level = d['high_temperature_level']
        if 'low_temperature_days' in d:
            o.low_temperature_days = d['low_temperature_days']
        if 'low_temperature_level' in d:
            o.low_temperature_level = d['low_temperature_level']
        if 'rainstorm_days' in d:
            o.rainstorm_days = d['rainstorm_days']
        if 'rainstorm_level' in d:
            o.rainstorm_level = d['rainstorm_level']
        if 'update_date' in d:
            o.update_date = d['update_date']
        return o


