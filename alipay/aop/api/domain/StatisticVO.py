#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StatisticVO(object):

    def __init__(self):
        self._abnormal = None
        self._end_time = None
        self._indicator = None
        self._range_type = None
        self._start_time = None
        self._sub_indicator = None
        self._value = None

    @property
    def abnormal(self):
        return self._abnormal

    @abnormal.setter
    def abnormal(self, value):
        self._abnormal = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def indicator(self):
        return self._indicator

    @indicator.setter
    def indicator(self, value):
        self._indicator = value
    @property
    def range_type(self):
        return self._range_type

    @range_type.setter
    def range_type(self, value):
        self._range_type = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_indicator(self):
        return self._sub_indicator

    @sub_indicator.setter
    def sub_indicator(self, value):
        self._sub_indicator = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal:
            if hasattr(self.abnormal, 'to_alipay_dict'):
                params['abnormal'] = self.abnormal.to_alipay_dict()
            else:
                params['abnormal'] = self.abnormal
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.indicator:
            if hasattr(self.indicator, 'to_alipay_dict'):
                params['indicator'] = self.indicator.to_alipay_dict()
            else:
                params['indicator'] = self.indicator
        if self.range_type:
            if hasattr(self.range_type, 'to_alipay_dict'):
                params['range_type'] = self.range_type.to_alipay_dict()
            else:
                params['range_type'] = self.range_type
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_indicator:
            if hasattr(self.sub_indicator, 'to_alipay_dict'):
                params['sub_indicator'] = self.sub_indicator.to_alipay_dict()
            else:
                params['sub_indicator'] = self.sub_indicator
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StatisticVO()
        if 'abnormal' in d:
            o.abnormal = d['abnormal']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'indicator' in d:
            o.indicator = d['indicator']
        if 'range_type' in d:
            o.range_type = d['range_type']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_indicator' in d:
            o.sub_indicator = d['sub_indicator']
        if 'value' in d:
            o.value = d['value']
        return o


