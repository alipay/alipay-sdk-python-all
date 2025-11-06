#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DrinkFrequency import DrinkFrequency


class AlcoholHistory(object):

    def __init__(self):
        self._alcohol_abstinence = None
        self._alcohol_type = None
        self._drink_frequency = None
        self._drinking = None
        self._drinking_time = None
        self._drinking_time_unit = None
        self._drinking_unit = None
        self._last_drink = None

    @property
    def alcohol_abstinence(self):
        return self._alcohol_abstinence

    @alcohol_abstinence.setter
    def alcohol_abstinence(self, value):
        self._alcohol_abstinence = value
    @property
    def alcohol_type(self):
        return self._alcohol_type

    @alcohol_type.setter
    def alcohol_type(self, value):
        self._alcohol_type = value
    @property
    def drink_frequency(self):
        return self._drink_frequency

    @drink_frequency.setter
    def drink_frequency(self, value):
        if isinstance(value, DrinkFrequency):
            self._drink_frequency = value
        else:
            self._drink_frequency = DrinkFrequency.from_alipay_dict(value)
    @property
    def drinking(self):
        return self._drinking

    @drinking.setter
    def drinking(self, value):
        self._drinking = value
    @property
    def drinking_time(self):
        return self._drinking_time

    @drinking_time.setter
    def drinking_time(self, value):
        self._drinking_time = value
    @property
    def drinking_time_unit(self):
        return self._drinking_time_unit

    @drinking_time_unit.setter
    def drinking_time_unit(self, value):
        self._drinking_time_unit = value
    @property
    def drinking_unit(self):
        return self._drinking_unit

    @drinking_unit.setter
    def drinking_unit(self, value):
        self._drinking_unit = value
    @property
    def last_drink(self):
        return self._last_drink

    @last_drink.setter
    def last_drink(self, value):
        self._last_drink = value


    def to_alipay_dict(self):
        params = dict()
        if self.alcohol_abstinence:
            if hasattr(self.alcohol_abstinence, 'to_alipay_dict'):
                params['alcohol_abstinence'] = self.alcohol_abstinence.to_alipay_dict()
            else:
                params['alcohol_abstinence'] = self.alcohol_abstinence
        if self.alcohol_type:
            if hasattr(self.alcohol_type, 'to_alipay_dict'):
                params['alcohol_type'] = self.alcohol_type.to_alipay_dict()
            else:
                params['alcohol_type'] = self.alcohol_type
        if self.drink_frequency:
            if hasattr(self.drink_frequency, 'to_alipay_dict'):
                params['drink_frequency'] = self.drink_frequency.to_alipay_dict()
            else:
                params['drink_frequency'] = self.drink_frequency
        if self.drinking:
            if hasattr(self.drinking, 'to_alipay_dict'):
                params['drinking'] = self.drinking.to_alipay_dict()
            else:
                params['drinking'] = self.drinking
        if self.drinking_time:
            if hasattr(self.drinking_time, 'to_alipay_dict'):
                params['drinking_time'] = self.drinking_time.to_alipay_dict()
            else:
                params['drinking_time'] = self.drinking_time
        if self.drinking_time_unit:
            if hasattr(self.drinking_time_unit, 'to_alipay_dict'):
                params['drinking_time_unit'] = self.drinking_time_unit.to_alipay_dict()
            else:
                params['drinking_time_unit'] = self.drinking_time_unit
        if self.drinking_unit:
            if hasattr(self.drinking_unit, 'to_alipay_dict'):
                params['drinking_unit'] = self.drinking_unit.to_alipay_dict()
            else:
                params['drinking_unit'] = self.drinking_unit
        if self.last_drink:
            if hasattr(self.last_drink, 'to_alipay_dict'):
                params['last_drink'] = self.last_drink.to_alipay_dict()
            else:
                params['last_drink'] = self.last_drink
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlcoholHistory()
        if 'alcohol_abstinence' in d:
            o.alcohol_abstinence = d['alcohol_abstinence']
        if 'alcohol_type' in d:
            o.alcohol_type = d['alcohol_type']
        if 'drink_frequency' in d:
            o.drink_frequency = d['drink_frequency']
        if 'drinking' in d:
            o.drinking = d['drinking']
        if 'drinking_time' in d:
            o.drinking_time = d['drinking_time']
        if 'drinking_time_unit' in d:
            o.drinking_time_unit = d['drinking_time_unit']
        if 'drinking_unit' in d:
            o.drinking_unit = d['drinking_unit']
        if 'last_drink' in d:
            o.last_drink = d['last_drink']
        return o


