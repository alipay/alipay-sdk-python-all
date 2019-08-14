#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPayChargePricingVO(object):

    def __init__(self):
        self._actual_charge = None
        self._actual_charge_rate = None
        self._charge_name = None
        self._origin_charge = None
        self._origin_charge_rate = None

    @property
    def actual_charge(self):
        return self._actual_charge

    @actual_charge.setter
    def actual_charge(self, value):
        self._actual_charge = value
    @property
    def actual_charge_rate(self):
        return self._actual_charge_rate

    @actual_charge_rate.setter
    def actual_charge_rate(self, value):
        self._actual_charge_rate = value
    @property
    def charge_name(self):
        return self._charge_name

    @charge_name.setter
    def charge_name(self, value):
        self._charge_name = value
    @property
    def origin_charge(self):
        return self._origin_charge

    @origin_charge.setter
    def origin_charge(self, value):
        self._origin_charge = value
    @property
    def origin_charge_rate(self):
        return self._origin_charge_rate

    @origin_charge_rate.setter
    def origin_charge_rate(self, value):
        self._origin_charge_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_charge:
            if hasattr(self.actual_charge, 'to_alipay_dict'):
                params['actual_charge'] = self.actual_charge.to_alipay_dict()
            else:
                params['actual_charge'] = self.actual_charge
        if self.actual_charge_rate:
            if hasattr(self.actual_charge_rate, 'to_alipay_dict'):
                params['actual_charge_rate'] = self.actual_charge_rate.to_alipay_dict()
            else:
                params['actual_charge_rate'] = self.actual_charge_rate
        if self.charge_name:
            if hasattr(self.charge_name, 'to_alipay_dict'):
                params['charge_name'] = self.charge_name.to_alipay_dict()
            else:
                params['charge_name'] = self.charge_name
        if self.origin_charge:
            if hasattr(self.origin_charge, 'to_alipay_dict'):
                params['origin_charge'] = self.origin_charge.to_alipay_dict()
            else:
                params['origin_charge'] = self.origin_charge
        if self.origin_charge_rate:
            if hasattr(self.origin_charge_rate, 'to_alipay_dict'):
                params['origin_charge_rate'] = self.origin_charge_rate.to_alipay_dict()
            else:
                params['origin_charge_rate'] = self.origin_charge_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayChargePricingVO()
        if 'actual_charge' in d:
            o.actual_charge = d['actual_charge']
        if 'actual_charge_rate' in d:
            o.actual_charge_rate = d['actual_charge_rate']
        if 'charge_name' in d:
            o.charge_name = d['charge_name']
        if 'origin_charge' in d:
            o.origin_charge = d['origin_charge']
        if 'origin_charge_rate' in d:
            o.origin_charge_rate = d['origin_charge_rate']
        return o


