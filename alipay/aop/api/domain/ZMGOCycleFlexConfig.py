#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOCycleFlexConfig(object):

    def __init__(self):
        self._cycle_flex_withhold_fee_name = None
        self._cycle_flex_withhold_max_price = None
        self._cycle_flex_withhold_total_period_count = None

    @property
    def cycle_flex_withhold_fee_name(self):
        return self._cycle_flex_withhold_fee_name

    @cycle_flex_withhold_fee_name.setter
    def cycle_flex_withhold_fee_name(self, value):
        self._cycle_flex_withhold_fee_name = value
    @property
    def cycle_flex_withhold_max_price(self):
        return self._cycle_flex_withhold_max_price

    @cycle_flex_withhold_max_price.setter
    def cycle_flex_withhold_max_price(self, value):
        self._cycle_flex_withhold_max_price = value
    @property
    def cycle_flex_withhold_total_period_count(self):
        return self._cycle_flex_withhold_total_period_count

    @cycle_flex_withhold_total_period_count.setter
    def cycle_flex_withhold_total_period_count(self, value):
        self._cycle_flex_withhold_total_period_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.cycle_flex_withhold_fee_name:
            if hasattr(self.cycle_flex_withhold_fee_name, 'to_alipay_dict'):
                params['cycle_flex_withhold_fee_name'] = self.cycle_flex_withhold_fee_name.to_alipay_dict()
            else:
                params['cycle_flex_withhold_fee_name'] = self.cycle_flex_withhold_fee_name
        if self.cycle_flex_withhold_max_price:
            if hasattr(self.cycle_flex_withhold_max_price, 'to_alipay_dict'):
                params['cycle_flex_withhold_max_price'] = self.cycle_flex_withhold_max_price.to_alipay_dict()
            else:
                params['cycle_flex_withhold_max_price'] = self.cycle_flex_withhold_max_price
        if self.cycle_flex_withhold_total_period_count:
            if hasattr(self.cycle_flex_withhold_total_period_count, 'to_alipay_dict'):
                params['cycle_flex_withhold_total_period_count'] = self.cycle_flex_withhold_total_period_count.to_alipay_dict()
            else:
                params['cycle_flex_withhold_total_period_count'] = self.cycle_flex_withhold_total_period_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOCycleFlexConfig()
        if 'cycle_flex_withhold_fee_name' in d:
            o.cycle_flex_withhold_fee_name = d['cycle_flex_withhold_fee_name']
        if 'cycle_flex_withhold_max_price' in d:
            o.cycle_flex_withhold_max_price = d['cycle_flex_withhold_max_price']
        if 'cycle_flex_withhold_total_period_count' in d:
            o.cycle_flex_withhold_total_period_count = d['cycle_flex_withhold_total_period_count']
        return o


