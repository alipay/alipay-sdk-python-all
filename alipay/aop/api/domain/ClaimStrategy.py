#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimStrategy(object):

    def __init__(self):
        self._accident_type = None
        self._biz_data = None
        self._constant = None
        self._end_section = None
        self._max_amount = None
        self._min_amount = None
        self._price_ratio = None
        self._start_compensation_time = None
        self._start_section = None
        self._time_ratio = None

    @property
    def accident_type(self):
        return self._accident_type

    @accident_type.setter
    def accident_type(self, value):
        self._accident_type = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def constant(self):
        return self._constant

    @constant.setter
    def constant(self, value):
        self._constant = value
    @property
    def end_section(self):
        return self._end_section

    @end_section.setter
    def end_section(self, value):
        self._end_section = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def price_ratio(self):
        return self._price_ratio

    @price_ratio.setter
    def price_ratio(self, value):
        self._price_ratio = value
    @property
    def start_compensation_time(self):
        return self._start_compensation_time

    @start_compensation_time.setter
    def start_compensation_time(self, value):
        self._start_compensation_time = value
    @property
    def start_section(self):
        return self._start_section

    @start_section.setter
    def start_section(self, value):
        self._start_section = value
    @property
    def time_ratio(self):
        return self._time_ratio

    @time_ratio.setter
    def time_ratio(self, value):
        self._time_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_type:
            if hasattr(self.accident_type, 'to_alipay_dict'):
                params['accident_type'] = self.accident_type.to_alipay_dict()
            else:
                params['accident_type'] = self.accident_type
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.constant:
            if hasattr(self.constant, 'to_alipay_dict'):
                params['constant'] = self.constant.to_alipay_dict()
            else:
                params['constant'] = self.constant
        if self.end_section:
            if hasattr(self.end_section, 'to_alipay_dict'):
                params['end_section'] = self.end_section.to_alipay_dict()
            else:
                params['end_section'] = self.end_section
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.price_ratio:
            if hasattr(self.price_ratio, 'to_alipay_dict'):
                params['price_ratio'] = self.price_ratio.to_alipay_dict()
            else:
                params['price_ratio'] = self.price_ratio
        if self.start_compensation_time:
            if hasattr(self.start_compensation_time, 'to_alipay_dict'):
                params['start_compensation_time'] = self.start_compensation_time.to_alipay_dict()
            else:
                params['start_compensation_time'] = self.start_compensation_time
        if self.start_section:
            if hasattr(self.start_section, 'to_alipay_dict'):
                params['start_section'] = self.start_section.to_alipay_dict()
            else:
                params['start_section'] = self.start_section
        if self.time_ratio:
            if hasattr(self.time_ratio, 'to_alipay_dict'):
                params['time_ratio'] = self.time_ratio.to_alipay_dict()
            else:
                params['time_ratio'] = self.time_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimStrategy()
        if 'accident_type' in d:
            o.accident_type = d['accident_type']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'constant' in d:
            o.constant = d['constant']
        if 'end_section' in d:
            o.end_section = d['end_section']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'price_ratio' in d:
            o.price_ratio = d['price_ratio']
        if 'start_compensation_time' in d:
            o.start_compensation_time = d['start_compensation_time']
        if 'start_section' in d:
            o.start_section = d['start_section']
        if 'time_ratio' in d:
            o.time_ratio = d['time_ratio']
        return o


