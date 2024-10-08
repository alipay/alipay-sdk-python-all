#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PolicyDetail(object):

    def __init__(self):
        self._deduct_amount = None
        self._deduct_type = None
        self._desc = None
        self._money_base = None
        self._time_base = None
        self._time_base_type = None

    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def deduct_type(self):
        return self._deduct_type

    @deduct_type.setter
    def deduct_type(self, value):
        self._deduct_type = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def money_base(self):
        return self._money_base

    @money_base.setter
    def money_base(self, value):
        self._money_base = value
    @property
    def time_base(self):
        return self._time_base

    @time_base.setter
    def time_base(self, value):
        self._time_base = value
    @property
    def time_base_type(self):
        return self._time_base_type

    @time_base_type.setter
    def time_base_type(self, value):
        self._time_base_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.deduct_type:
            if hasattr(self.deduct_type, 'to_alipay_dict'):
                params['deduct_type'] = self.deduct_type.to_alipay_dict()
            else:
                params['deduct_type'] = self.deduct_type
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.money_base:
            if hasattr(self.money_base, 'to_alipay_dict'):
                params['money_base'] = self.money_base.to_alipay_dict()
            else:
                params['money_base'] = self.money_base
        if self.time_base:
            if hasattr(self.time_base, 'to_alipay_dict'):
                params['time_base'] = self.time_base.to_alipay_dict()
            else:
                params['time_base'] = self.time_base
        if self.time_base_type:
            if hasattr(self.time_base_type, 'to_alipay_dict'):
                params['time_base_type'] = self.time_base_type.to_alipay_dict()
            else:
                params['time_base_type'] = self.time_base_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyDetail()
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'deduct_type' in d:
            o.deduct_type = d['deduct_type']
        if 'desc' in d:
            o.desc = d['desc']
        if 'money_base' in d:
            o.money_base = d['money_base']
        if 'time_base' in d:
            o.time_base = d['time_base']
        if 'time_base_type' in d:
            o.time_base_type = d['time_base_type']
        return o


