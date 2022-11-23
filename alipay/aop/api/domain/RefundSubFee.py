#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RefundSubFee(object):

    def __init__(self):
        self._refund_charge_fee = None
        self._switch_fee_rate = None

    @property
    def refund_charge_fee(self):
        return self._refund_charge_fee

    @refund_charge_fee.setter
    def refund_charge_fee(self, value):
        self._refund_charge_fee = value
    @property
    def switch_fee_rate(self):
        return self._switch_fee_rate

    @switch_fee_rate.setter
    def switch_fee_rate(self, value):
        self._switch_fee_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_charge_fee:
            if hasattr(self.refund_charge_fee, 'to_alipay_dict'):
                params['refund_charge_fee'] = self.refund_charge_fee.to_alipay_dict()
            else:
                params['refund_charge_fee'] = self.refund_charge_fee
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
        o = RefundSubFee()
        if 'refund_charge_fee' in d:
            o.refund_charge_fee = d['refund_charge_fee']
        if 'switch_fee_rate' in d:
            o.switch_fee_rate = d['switch_fee_rate']
        return o


