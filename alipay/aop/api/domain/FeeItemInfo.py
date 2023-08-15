#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeeItemInfo(object):

    def __init__(self):
        self._fee_item_code = None
        self._fee_item_name = None
        self._percent = None
        self._total_value = None
        self._unit = None
        self._used_value = None

    @property
    def fee_item_code(self):
        return self._fee_item_code

    @fee_item_code.setter
    def fee_item_code(self, value):
        self._fee_item_code = value
    @property
    def fee_item_name(self):
        return self._fee_item_name

    @fee_item_name.setter
    def fee_item_name(self, value):
        self._fee_item_name = value
    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        self._percent = value
    @property
    def total_value(self):
        return self._total_value

    @total_value.setter
    def total_value(self, value):
        self._total_value = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def used_value(self):
        return self._used_value

    @used_value.setter
    def used_value(self, value):
        self._used_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_item_code:
            if hasattr(self.fee_item_code, 'to_alipay_dict'):
                params['fee_item_code'] = self.fee_item_code.to_alipay_dict()
            else:
                params['fee_item_code'] = self.fee_item_code
        if self.fee_item_name:
            if hasattr(self.fee_item_name, 'to_alipay_dict'):
                params['fee_item_name'] = self.fee_item_name.to_alipay_dict()
            else:
                params['fee_item_name'] = self.fee_item_name
        if self.percent:
            if hasattr(self.percent, 'to_alipay_dict'):
                params['percent'] = self.percent.to_alipay_dict()
            else:
                params['percent'] = self.percent
        if self.total_value:
            if hasattr(self.total_value, 'to_alipay_dict'):
                params['total_value'] = self.total_value.to_alipay_dict()
            else:
                params['total_value'] = self.total_value
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.used_value:
            if hasattr(self.used_value, 'to_alipay_dict'):
                params['used_value'] = self.used_value.to_alipay_dict()
            else:
                params['used_value'] = self.used_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeeItemInfo()
        if 'fee_item_code' in d:
            o.fee_item_code = d['fee_item_code']
        if 'fee_item_name' in d:
            o.fee_item_name = d['fee_item_name']
        if 'percent' in d:
            o.percent = d['percent']
        if 'total_value' in d:
            o.total_value = d['total_value']
        if 'unit' in d:
            o.unit = d['unit']
        if 'used_value' in d:
            o.used_value = d['used_value']
        return o


