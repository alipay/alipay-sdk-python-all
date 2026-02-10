#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RoboAirConditionerInfo(object):

    def __init__(self):
        self._air_ability = None
        self._max_temperature = None
        self._min_temperature = None
        self._open_status = None
        self._temperature = None

    @property
    def air_ability(self):
        return self._air_ability

    @air_ability.setter
    def air_ability(self, value):
        self._air_ability = value
    @property
    def max_temperature(self):
        return self._max_temperature

    @max_temperature.setter
    def max_temperature(self, value):
        self._max_temperature = value
    @property
    def min_temperature(self):
        return self._min_temperature

    @min_temperature.setter
    def min_temperature(self, value):
        self._min_temperature = value
    @property
    def open_status(self):
        return self._open_status

    @open_status.setter
    def open_status(self, value):
        self._open_status = value
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value


    def to_alipay_dict(self):
        params = dict()
        if self.air_ability:
            if hasattr(self.air_ability, 'to_alipay_dict'):
                params['air_ability'] = self.air_ability.to_alipay_dict()
            else:
                params['air_ability'] = self.air_ability
        if self.max_temperature:
            if hasattr(self.max_temperature, 'to_alipay_dict'):
                params['max_temperature'] = self.max_temperature.to_alipay_dict()
            else:
                params['max_temperature'] = self.max_temperature
        if self.min_temperature:
            if hasattr(self.min_temperature, 'to_alipay_dict'):
                params['min_temperature'] = self.min_temperature.to_alipay_dict()
            else:
                params['min_temperature'] = self.min_temperature
        if self.open_status:
            if hasattr(self.open_status, 'to_alipay_dict'):
                params['open_status'] = self.open_status.to_alipay_dict()
            else:
                params['open_status'] = self.open_status
        if self.temperature:
            if hasattr(self.temperature, 'to_alipay_dict'):
                params['temperature'] = self.temperature.to_alipay_dict()
            else:
                params['temperature'] = self.temperature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RoboAirConditionerInfo()
        if 'air_ability' in d:
            o.air_ability = d['air_ability']
        if 'max_temperature' in d:
            o.max_temperature = d['max_temperature']
        if 'min_temperature' in d:
            o.min_temperature = d['min_temperature']
        if 'open_status' in d:
            o.open_status = d['open_status']
        if 'temperature' in d:
            o.temperature = d['temperature']
        return o


