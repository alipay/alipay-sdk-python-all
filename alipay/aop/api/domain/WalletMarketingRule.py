#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalletMarketingRule(object):

    def __init__(self):
        self._ma_type = None
        self._ma_value = None
        self._refund_marketing_amount = None

    @property
    def ma_type(self):
        return self._ma_type

    @ma_type.setter
    def ma_type(self, value):
        self._ma_type = value
    @property
    def ma_value(self):
        return self._ma_value

    @ma_value.setter
    def ma_value(self, value):
        self._ma_value = value
    @property
    def refund_marketing_amount(self):
        return self._refund_marketing_amount

    @refund_marketing_amount.setter
    def refund_marketing_amount(self, value):
        self._refund_marketing_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.ma_type:
            if hasattr(self.ma_type, 'to_alipay_dict'):
                params['ma_type'] = self.ma_type.to_alipay_dict()
            else:
                params['ma_type'] = self.ma_type
        if self.ma_value:
            if hasattr(self.ma_value, 'to_alipay_dict'):
                params['ma_value'] = self.ma_value.to_alipay_dict()
            else:
                params['ma_value'] = self.ma_value
        if self.refund_marketing_amount:
            if hasattr(self.refund_marketing_amount, 'to_alipay_dict'):
                params['refund_marketing_amount'] = self.refund_marketing_amount.to_alipay_dict()
            else:
                params['refund_marketing_amount'] = self.refund_marketing_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletMarketingRule()
        if 'ma_type' in d:
            o.ma_type = d['ma_type']
        if 'ma_value' in d:
            o.ma_value = d['ma_value']
        if 'refund_marketing_amount' in d:
            o.refund_marketing_amount = d['refund_marketing_amount']
        return o


