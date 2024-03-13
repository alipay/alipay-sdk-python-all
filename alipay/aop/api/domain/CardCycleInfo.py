#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardCycleInfo(object):

    def __init__(self):
        self._cycle_charge_start_time = None
        self._cycle_charge_type = None
        self._cycle_range = None
        self._cycle_type = None
        self._cycle_value = None

    @property
    def cycle_charge_start_time(self):
        return self._cycle_charge_start_time

    @cycle_charge_start_time.setter
    def cycle_charge_start_time(self, value):
        self._cycle_charge_start_time = value
    @property
    def cycle_charge_type(self):
        return self._cycle_charge_type

    @cycle_charge_type.setter
    def cycle_charge_type(self, value):
        self._cycle_charge_type = value
    @property
    def cycle_range(self):
        return self._cycle_range

    @cycle_range.setter
    def cycle_range(self, value):
        self._cycle_range = value
    @property
    def cycle_type(self):
        return self._cycle_type

    @cycle_type.setter
    def cycle_type(self, value):
        self._cycle_type = value
    @property
    def cycle_value(self):
        return self._cycle_value

    @cycle_value.setter
    def cycle_value(self, value):
        self._cycle_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_charge_start_time:
            if hasattr(self.cycle_charge_start_time, 'to_alipay_dict'):
                params['cycle_charge_start_time'] = self.cycle_charge_start_time.to_alipay_dict()
            else:
                params['cycle_charge_start_time'] = self.cycle_charge_start_time
        if self.cycle_charge_type:
            if hasattr(self.cycle_charge_type, 'to_alipay_dict'):
                params['cycle_charge_type'] = self.cycle_charge_type.to_alipay_dict()
            else:
                params['cycle_charge_type'] = self.cycle_charge_type
        if self.cycle_range:
            if hasattr(self.cycle_range, 'to_alipay_dict'):
                params['cycle_range'] = self.cycle_range.to_alipay_dict()
            else:
                params['cycle_range'] = self.cycle_range
        if self.cycle_type:
            if hasattr(self.cycle_type, 'to_alipay_dict'):
                params['cycle_type'] = self.cycle_type.to_alipay_dict()
            else:
                params['cycle_type'] = self.cycle_type
        if self.cycle_value:
            if hasattr(self.cycle_value, 'to_alipay_dict'):
                params['cycle_value'] = self.cycle_value.to_alipay_dict()
            else:
                params['cycle_value'] = self.cycle_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardCycleInfo()
        if 'cycle_charge_start_time' in d:
            o.cycle_charge_start_time = d['cycle_charge_start_time']
        if 'cycle_charge_type' in d:
            o.cycle_charge_type = d['cycle_charge_type']
        if 'cycle_range' in d:
            o.cycle_range = d['cycle_range']
        if 'cycle_type' in d:
            o.cycle_type = d['cycle_type']
        if 'cycle_value' in d:
            o.cycle_value = d['cycle_value']
        return o


