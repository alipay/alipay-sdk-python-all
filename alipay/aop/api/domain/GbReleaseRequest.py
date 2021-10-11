#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GbReleaseRequest(object):

    def __init__(self):
        self._amount = None
        self._biz_date = None
        self._biz_name = None
        self._biz_uk_id = None
        self._budget_use_type = None
        self._currency = None
        self._group_budget_code = None
        self._tax_included = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def biz_uk_id(self):
        return self._biz_uk_id

    @biz_uk_id.setter
    def biz_uk_id(self, value):
        self._biz_uk_id = value
    @property
    def budget_use_type(self):
        return self._budget_use_type

    @budget_use_type.setter
    def budget_use_type(self, value):
        self._budget_use_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def group_budget_code(self):
        return self._group_budget_code

    @group_budget_code.setter
    def group_budget_code(self, value):
        self._group_budget_code = value
    @property
    def tax_included(self):
        return self._tax_included

    @tax_included.setter
    def tax_included(self, value):
        self._tax_included = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.biz_uk_id:
            if hasattr(self.biz_uk_id, 'to_alipay_dict'):
                params['biz_uk_id'] = self.biz_uk_id.to_alipay_dict()
            else:
                params['biz_uk_id'] = self.biz_uk_id
        if self.budget_use_type:
            if hasattr(self.budget_use_type, 'to_alipay_dict'):
                params['budget_use_type'] = self.budget_use_type.to_alipay_dict()
            else:
                params['budget_use_type'] = self.budget_use_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.group_budget_code:
            if hasattr(self.group_budget_code, 'to_alipay_dict'):
                params['group_budget_code'] = self.group_budget_code.to_alipay_dict()
            else:
                params['group_budget_code'] = self.group_budget_code
        if self.tax_included:
            if hasattr(self.tax_included, 'to_alipay_dict'):
                params['tax_included'] = self.tax_included.to_alipay_dict()
            else:
                params['tax_included'] = self.tax_included
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GbReleaseRequest()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'biz_uk_id' in d:
            o.biz_uk_id = d['biz_uk_id']
        if 'budget_use_type' in d:
            o.budget_use_type = d['budget_use_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'group_budget_code' in d:
            o.group_budget_code = d['group_budget_code']
        if 'tax_included' in d:
            o.tax_included = d['tax_included']
        return o


