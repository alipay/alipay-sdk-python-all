#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FixedRentBillingRuleDTO(object):

    def __init__(self):
        self._period_num = None
        self._period_rent_amount = None
        self._period_unit = None
        self._period_unit_num = None
        self._rent_amount = None
        self._type = None

    @property
    def period_num(self):
        return self._period_num

    @period_num.setter
    def period_num(self, value):
        self._period_num = value
    @property
    def period_rent_amount(self):
        return self._period_rent_amount

    @period_rent_amount.setter
    def period_rent_amount(self, value):
        self._period_rent_amount = value
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value
    @property
    def period_unit_num(self):
        return self._period_unit_num

    @period_unit_num.setter
    def period_unit_num(self, value):
        self._period_unit_num = value
    @property
    def rent_amount(self):
        return self._rent_amount

    @rent_amount.setter
    def rent_amount(self, value):
        self._rent_amount = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_num:
            if hasattr(self.period_num, 'to_alipay_dict'):
                params['period_num'] = self.period_num.to_alipay_dict()
            else:
                params['period_num'] = self.period_num
        if self.period_rent_amount:
            if hasattr(self.period_rent_amount, 'to_alipay_dict'):
                params['period_rent_amount'] = self.period_rent_amount.to_alipay_dict()
            else:
                params['period_rent_amount'] = self.period_rent_amount
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        if self.period_unit_num:
            if hasattr(self.period_unit_num, 'to_alipay_dict'):
                params['period_unit_num'] = self.period_unit_num.to_alipay_dict()
            else:
                params['period_unit_num'] = self.period_unit_num
        if self.rent_amount:
            if hasattr(self.rent_amount, 'to_alipay_dict'):
                params['rent_amount'] = self.rent_amount.to_alipay_dict()
            else:
                params['rent_amount'] = self.rent_amount
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FixedRentBillingRuleDTO()
        if 'period_num' in d:
            o.period_num = d['period_num']
        if 'period_rent_amount' in d:
            o.period_rent_amount = d['period_rent_amount']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        if 'period_unit_num' in d:
            o.period_unit_num = d['period_unit_num']
        if 'rent_amount' in d:
            o.rent_amount = d['rent_amount']
        if 'type' in d:
            o.type = d['type']
        return o


