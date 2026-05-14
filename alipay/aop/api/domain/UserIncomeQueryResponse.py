#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserIncomeQueryResponse(object):

    def __init__(self):
        self._amount = None
        self._biz_month = None
        self._currency_code = None
        self._passport_id = None
        self._platform_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_month(self):
        return self._biz_month

    @biz_month.setter
    def biz_month(self, value):
        self._biz_month = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_month:
            if hasattr(self.biz_month, 'to_alipay_dict'):
                params['biz_month'] = self.biz_month.to_alipay_dict()
            else:
                params['biz_month'] = self.biz_month
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserIncomeQueryResponse()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_month' in d:
            o.biz_month = d['biz_month']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        return o


