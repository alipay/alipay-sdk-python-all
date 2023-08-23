#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FuelVoucherInfo(object):

    def __init__(self):
        self._activity_code = None
        self._activity_type = None
        self._alipay_amount = None
        self._amount = None
        self._merchant_amount = None
        self._voucher_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def alipay_amount(self):
        return self._alipay_amount

    @alipay_amount.setter
    def alipay_amount(self, value):
        self._alipay_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def merchant_amount(self):
        return self._merchant_amount

    @merchant_amount.setter
    def merchant_amount(self, value):
        self._merchant_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.alipay_amount:
            if hasattr(self.alipay_amount, 'to_alipay_dict'):
                params['alipay_amount'] = self.alipay_amount.to_alipay_dict()
            else:
                params['alipay_amount'] = self.alipay_amount
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.merchant_amount:
            if hasattr(self.merchant_amount, 'to_alipay_dict'):
                params['merchant_amount'] = self.merchant_amount.to_alipay_dict()
            else:
                params['merchant_amount'] = self.merchant_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FuelVoucherInfo()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'alipay_amount' in d:
            o.alipay_amount = d['alipay_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'merchant_amount' in d:
            o.merchant_amount = d['merchant_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


