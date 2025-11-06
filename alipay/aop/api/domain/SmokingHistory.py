#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmokingHistory(object):

    def __init__(self):
        self._daily_smoking = None
        self._daily_smoking_unit = None
        self._last_smoking = None
        self._smoking_cessation = None
        self._smoking_time = None
        self._smoking_time_unit = None

    @property
    def daily_smoking(self):
        return self._daily_smoking

    @daily_smoking.setter
    def daily_smoking(self, value):
        self._daily_smoking = value
    @property
    def daily_smoking_unit(self):
        return self._daily_smoking_unit

    @daily_smoking_unit.setter
    def daily_smoking_unit(self, value):
        self._daily_smoking_unit = value
    @property
    def last_smoking(self):
        return self._last_smoking

    @last_smoking.setter
    def last_smoking(self, value):
        self._last_smoking = value
    @property
    def smoking_cessation(self):
        return self._smoking_cessation

    @smoking_cessation.setter
    def smoking_cessation(self, value):
        self._smoking_cessation = value
    @property
    def smoking_time(self):
        return self._smoking_time

    @smoking_time.setter
    def smoking_time(self, value):
        self._smoking_time = value
    @property
    def smoking_time_unit(self):
        return self._smoking_time_unit

    @smoking_time_unit.setter
    def smoking_time_unit(self, value):
        self._smoking_time_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.daily_smoking:
            if hasattr(self.daily_smoking, 'to_alipay_dict'):
                params['daily_smoking'] = self.daily_smoking.to_alipay_dict()
            else:
                params['daily_smoking'] = self.daily_smoking
        if self.daily_smoking_unit:
            if hasattr(self.daily_smoking_unit, 'to_alipay_dict'):
                params['daily_smoking_unit'] = self.daily_smoking_unit.to_alipay_dict()
            else:
                params['daily_smoking_unit'] = self.daily_smoking_unit
        if self.last_smoking:
            if hasattr(self.last_smoking, 'to_alipay_dict'):
                params['last_smoking'] = self.last_smoking.to_alipay_dict()
            else:
                params['last_smoking'] = self.last_smoking
        if self.smoking_cessation:
            if hasattr(self.smoking_cessation, 'to_alipay_dict'):
                params['smoking_cessation'] = self.smoking_cessation.to_alipay_dict()
            else:
                params['smoking_cessation'] = self.smoking_cessation
        if self.smoking_time:
            if hasattr(self.smoking_time, 'to_alipay_dict'):
                params['smoking_time'] = self.smoking_time.to_alipay_dict()
            else:
                params['smoking_time'] = self.smoking_time
        if self.smoking_time_unit:
            if hasattr(self.smoking_time_unit, 'to_alipay_dict'):
                params['smoking_time_unit'] = self.smoking_time_unit.to_alipay_dict()
            else:
                params['smoking_time_unit'] = self.smoking_time_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmokingHistory()
        if 'daily_smoking' in d:
            o.daily_smoking = d['daily_smoking']
        if 'daily_smoking_unit' in d:
            o.daily_smoking_unit = d['daily_smoking_unit']
        if 'last_smoking' in d:
            o.last_smoking = d['last_smoking']
        if 'smoking_cessation' in d:
            o.smoking_cessation = d['smoking_cessation']
        if 'smoking_time' in d:
            o.smoking_time = d['smoking_time']
        if 'smoking_time_unit' in d:
            o.smoking_time_unit = d['smoking_time_unit']
        return o


