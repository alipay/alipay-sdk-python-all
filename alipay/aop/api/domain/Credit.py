#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPricing import CreditPricing


class Credit(object):

    def __init__(self):
        self._available_amt = None
        self._credit_amt = None
        self._credit_pricing_list = None
        self._credit_update_reason = None
        self._default_credit = None
        self._expire_time = None
        self._loan_type = None
        self._multiple_lend = None
        self._product_code = None
        self._usable_status = None
        self._used_amt = None

    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value
    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
    @property
    def credit_pricing_list(self):
        return self._credit_pricing_list

    @credit_pricing_list.setter
    def credit_pricing_list(self, value):
        if isinstance(value, list):
            self._credit_pricing_list = list()
            for i in value:
                if isinstance(i, CreditPricing):
                    self._credit_pricing_list.append(i)
                else:
                    self._credit_pricing_list.append(CreditPricing.from_alipay_dict(i))
    @property
    def credit_update_reason(self):
        return self._credit_update_reason

    @credit_update_reason.setter
    def credit_update_reason(self, value):
        self._credit_update_reason = value
    @property
    def default_credit(self):
        return self._default_credit

    @default_credit.setter
    def default_credit(self, value):
        self._default_credit = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def loan_type(self):
        return self._loan_type

    @loan_type.setter
    def loan_type(self, value):
        self._loan_type = value
    @property
    def multiple_lend(self):
        return self._multiple_lend

    @multiple_lend.setter
    def multiple_lend(self, value):
        self._multiple_lend = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def usable_status(self):
        return self._usable_status

    @usable_status.setter
    def usable_status(self, value):
        self._usable_status = value
    @property
    def used_amt(self):
        return self._used_amt

    @used_amt.setter
    def used_amt(self, value):
        self._used_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amt:
            if hasattr(self.available_amt, 'to_alipay_dict'):
                params['available_amt'] = self.available_amt.to_alipay_dict()
            else:
                params['available_amt'] = self.available_amt
        if self.credit_amt:
            if hasattr(self.credit_amt, 'to_alipay_dict'):
                params['credit_amt'] = self.credit_amt.to_alipay_dict()
            else:
                params['credit_amt'] = self.credit_amt
        if self.credit_pricing_list:
            if isinstance(self.credit_pricing_list, list):
                for i in range(0, len(self.credit_pricing_list)):
                    element = self.credit_pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_pricing_list, 'to_alipay_dict'):
                params['credit_pricing_list'] = self.credit_pricing_list.to_alipay_dict()
            else:
                params['credit_pricing_list'] = self.credit_pricing_list
        if self.credit_update_reason:
            if hasattr(self.credit_update_reason, 'to_alipay_dict'):
                params['credit_update_reason'] = self.credit_update_reason.to_alipay_dict()
            else:
                params['credit_update_reason'] = self.credit_update_reason
        if self.default_credit:
            if hasattr(self.default_credit, 'to_alipay_dict'):
                params['default_credit'] = self.default_credit.to_alipay_dict()
            else:
                params['default_credit'] = self.default_credit
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.loan_type:
            if hasattr(self.loan_type, 'to_alipay_dict'):
                params['loan_type'] = self.loan_type.to_alipay_dict()
            else:
                params['loan_type'] = self.loan_type
        if self.multiple_lend:
            if hasattr(self.multiple_lend, 'to_alipay_dict'):
                params['multiple_lend'] = self.multiple_lend.to_alipay_dict()
            else:
                params['multiple_lend'] = self.multiple_lend
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.usable_status:
            if hasattr(self.usable_status, 'to_alipay_dict'):
                params['usable_status'] = self.usable_status.to_alipay_dict()
            else:
                params['usable_status'] = self.usable_status
        if self.used_amt:
            if hasattr(self.used_amt, 'to_alipay_dict'):
                params['used_amt'] = self.used_amt.to_alipay_dict()
            else:
                params['used_amt'] = self.used_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Credit()
        if 'available_amt' in d:
            o.available_amt = d['available_amt']
        if 'credit_amt' in d:
            o.credit_amt = d['credit_amt']
        if 'credit_pricing_list' in d:
            o.credit_pricing_list = d['credit_pricing_list']
        if 'credit_update_reason' in d:
            o.credit_update_reason = d['credit_update_reason']
        if 'default_credit' in d:
            o.default_credit = d['default_credit']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'loan_type' in d:
            o.loan_type = d['loan_type']
        if 'multiple_lend' in d:
            o.multiple_lend = d['multiple_lend']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'usable_status' in d:
            o.usable_status = d['usable_status']
        if 'used_amt' in d:
            o.used_amt = d['used_amt']
        return o


