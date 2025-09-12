#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorProductInfoDTO(object):

    def __init__(self):
        self._apr = None
        self._day_rate = None
        self._early_repay = None
        self._repay_method = None
        self._temp_apr = None
        self._temp_day_rate = None
        self._temp_price_due_time = None
        self._term_nums = None

    @property
    def apr(self):
        return self._apr

    @apr.setter
    def apr(self, value):
        self._apr = value
    @property
    def day_rate(self):
        return self._day_rate

    @day_rate.setter
    def day_rate(self, value):
        self._day_rate = value
    @property
    def early_repay(self):
        return self._early_repay

    @early_repay.setter
    def early_repay(self, value):
        self._early_repay = value
    @property
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
    @property
    def temp_apr(self):
        return self._temp_apr

    @temp_apr.setter
    def temp_apr(self, value):
        self._temp_apr = value
    @property
    def temp_day_rate(self):
        return self._temp_day_rate

    @temp_day_rate.setter
    def temp_day_rate(self, value):
        self._temp_day_rate = value
    @property
    def temp_price_due_time(self):
        return self._temp_price_due_time

    @temp_price_due_time.setter
    def temp_price_due_time(self, value):
        self._temp_price_due_time = value
    @property
    def term_nums(self):
        return self._term_nums

    @term_nums.setter
    def term_nums(self, value):
        if isinstance(value, list):
            self._term_nums = list()
            for i in value:
                self._term_nums.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.apr:
            if hasattr(self.apr, 'to_alipay_dict'):
                params['apr'] = self.apr.to_alipay_dict()
            else:
                params['apr'] = self.apr
        if self.day_rate:
            if hasattr(self.day_rate, 'to_alipay_dict'):
                params['day_rate'] = self.day_rate.to_alipay_dict()
            else:
                params['day_rate'] = self.day_rate
        if self.early_repay:
            if hasattr(self.early_repay, 'to_alipay_dict'):
                params['early_repay'] = self.early_repay.to_alipay_dict()
            else:
                params['early_repay'] = self.early_repay
        if self.repay_method:
            if hasattr(self.repay_method, 'to_alipay_dict'):
                params['repay_method'] = self.repay_method.to_alipay_dict()
            else:
                params['repay_method'] = self.repay_method
        if self.temp_apr:
            if hasattr(self.temp_apr, 'to_alipay_dict'):
                params['temp_apr'] = self.temp_apr.to_alipay_dict()
            else:
                params['temp_apr'] = self.temp_apr
        if self.temp_day_rate:
            if hasattr(self.temp_day_rate, 'to_alipay_dict'):
                params['temp_day_rate'] = self.temp_day_rate.to_alipay_dict()
            else:
                params['temp_day_rate'] = self.temp_day_rate
        if self.temp_price_due_time:
            if hasattr(self.temp_price_due_time, 'to_alipay_dict'):
                params['temp_price_due_time'] = self.temp_price_due_time.to_alipay_dict()
            else:
                params['temp_price_due_time'] = self.temp_price_due_time
        if self.term_nums:
            if isinstance(self.term_nums, list):
                for i in range(0, len(self.term_nums)):
                    element = self.term_nums[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.term_nums[i] = element.to_alipay_dict()
            if hasattr(self.term_nums, 'to_alipay_dict'):
                params['term_nums'] = self.term_nums.to_alipay_dict()
            else:
                params['term_nums'] = self.term_nums
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorProductInfoDTO()
        if 'apr' in d:
            o.apr = d['apr']
        if 'day_rate' in d:
            o.day_rate = d['day_rate']
        if 'early_repay' in d:
            o.early_repay = d['early_repay']
        if 'repay_method' in d:
            o.repay_method = d['repay_method']
        if 'temp_apr' in d:
            o.temp_apr = d['temp_apr']
        if 'temp_day_rate' in d:
            o.temp_day_rate = d['temp_day_rate']
        if 'temp_price_due_time' in d:
            o.temp_price_due_time = d['temp_price_due_time']
        if 'term_nums' in d:
            o.term_nums = d['term_nums']
        return o


