#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubFee(object):

    def __init__(self):
        self._charge_fee = None
        self._original_charge_fee = None
        self._switch_fee_rate = None

    @property
    def charge_fee(self):
        return self._charge_fee

    @charge_fee.setter
    def charge_fee(self, value):
        self._charge_fee = value
    @property
    def original_charge_fee(self):
        return self._original_charge_fee

    @original_charge_fee.setter
    def original_charge_fee(self, value):
        self._original_charge_fee = value
    @property
    def switch_fee_rate(self):
        return self._switch_fee_rate

    @switch_fee_rate.setter
    def switch_fee_rate(self, value):
        self._switch_fee_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.charge_fee:
            if hasattr(self.charge_fee, 'to_alipay_dict'):
                params['charge_fee'] = self.charge_fee.to_alipay_dict()
            else:
                params['charge_fee'] = self.charge_fee
        if self.original_charge_fee:
            if hasattr(self.original_charge_fee, 'to_alipay_dict'):
                params['original_charge_fee'] = self.original_charge_fee.to_alipay_dict()
            else:
                params['original_charge_fee'] = self.original_charge_fee
        if self.switch_fee_rate:
            if hasattr(self.switch_fee_rate, 'to_alipay_dict'):
                params['switch_fee_rate'] = self.switch_fee_rate.to_alipay_dict()
            else:
                params['switch_fee_rate'] = self.switch_fee_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubFee()
        if 'charge_fee' in d:
            o.charge_fee = d['charge_fee']
        if 'original_charge_fee' in d:
            o.original_charge_fee = d['original_charge_fee']
        if 'switch_fee_rate' in d:
            o.switch_fee_rate = d['switch_fee_rate']
        return o


