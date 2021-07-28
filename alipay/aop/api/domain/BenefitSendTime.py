#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitSendTime(object):

    def __init__(self):
        self._cycle_period_type = None
        self._cycle_period_value = None
        self._send_begin_time = None
        self._send_end_time = None
        self._sub_cycle_period_type = None
        self._sub_cycle_period_value = None

    @property
    def cycle_period_type(self):
        return self._cycle_period_type

    @cycle_period_type.setter
    def cycle_period_type(self, value):
        self._cycle_period_type = value
    @property
    def cycle_period_value(self):
        return self._cycle_period_value

    @cycle_period_value.setter
    def cycle_period_value(self, value):
        self._cycle_period_value = value
    @property
    def send_begin_time(self):
        return self._send_begin_time

    @send_begin_time.setter
    def send_begin_time(self, value):
        self._send_begin_time = value
    @property
    def send_end_time(self):
        return self._send_end_time

    @send_end_time.setter
    def send_end_time(self, value):
        self._send_end_time = value
    @property
    def sub_cycle_period_type(self):
        return self._sub_cycle_period_type

    @sub_cycle_period_type.setter
    def sub_cycle_period_type(self, value):
        self._sub_cycle_period_type = value
    @property
    def sub_cycle_period_value(self):
        return self._sub_cycle_period_value

    @sub_cycle_period_value.setter
    def sub_cycle_period_value(self, value):
        if isinstance(value, list):
            self._sub_cycle_period_value = list()
            for i in value:
                self._sub_cycle_period_value.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_period_type:
            if hasattr(self.cycle_period_type, 'to_alipay_dict'):
                params['cycle_period_type'] = self.cycle_period_type.to_alipay_dict()
            else:
                params['cycle_period_type'] = self.cycle_period_type
        if self.cycle_period_value:
            if hasattr(self.cycle_period_value, 'to_alipay_dict'):
                params['cycle_period_value'] = self.cycle_period_value.to_alipay_dict()
            else:
                params['cycle_period_value'] = self.cycle_period_value
        if self.send_begin_time:
            if hasattr(self.send_begin_time, 'to_alipay_dict'):
                params['send_begin_time'] = self.send_begin_time.to_alipay_dict()
            else:
                params['send_begin_time'] = self.send_begin_time
        if self.send_end_time:
            if hasattr(self.send_end_time, 'to_alipay_dict'):
                params['send_end_time'] = self.send_end_time.to_alipay_dict()
            else:
                params['send_end_time'] = self.send_end_time
        if self.sub_cycle_period_type:
            if hasattr(self.sub_cycle_period_type, 'to_alipay_dict'):
                params['sub_cycle_period_type'] = self.sub_cycle_period_type.to_alipay_dict()
            else:
                params['sub_cycle_period_type'] = self.sub_cycle_period_type
        if self.sub_cycle_period_value:
            if isinstance(self.sub_cycle_period_value, list):
                for i in range(0, len(self.sub_cycle_period_value)):
                    element = self.sub_cycle_period_value[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_cycle_period_value[i] = element.to_alipay_dict()
            if hasattr(self.sub_cycle_period_value, 'to_alipay_dict'):
                params['sub_cycle_period_value'] = self.sub_cycle_period_value.to_alipay_dict()
            else:
                params['sub_cycle_period_value'] = self.sub_cycle_period_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitSendTime()
        if 'cycle_period_type' in d:
            o.cycle_period_type = d['cycle_period_type']
        if 'cycle_period_value' in d:
            o.cycle_period_value = d['cycle_period_value']
        if 'send_begin_time' in d:
            o.send_begin_time = d['send_begin_time']
        if 'send_end_time' in d:
            o.send_end_time = d['send_end_time']
        if 'sub_cycle_period_type' in d:
            o.sub_cycle_period_type = d['sub_cycle_period_type']
        if 'sub_cycle_period_value' in d:
            o.sub_cycle_period_value = d['sub_cycle_period_value']
        return o


