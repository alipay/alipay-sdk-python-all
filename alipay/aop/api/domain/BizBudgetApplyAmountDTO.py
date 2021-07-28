#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizBudgetApplyAmountDTO(object):

    def __init__(self):
        self._biz_budget_apply_code = None
        self._consumed_amount = None
        self._consumed_amount_currency = None
        self._remain_amount = None
        self._remain_amount_currency = None

    @property
    def biz_budget_apply_code(self):
        return self._biz_budget_apply_code

    @biz_budget_apply_code.setter
    def biz_budget_apply_code(self, value):
        self._biz_budget_apply_code = value
    @property
    def consumed_amount(self):
        return self._consumed_amount

    @consumed_amount.setter
    def consumed_amount(self, value):
        self._consumed_amount = value
    @property
    def consumed_amount_currency(self):
        return self._consumed_amount_currency

    @consumed_amount_currency.setter
    def consumed_amount_currency(self, value):
        self._consumed_amount_currency = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def remain_amount_currency(self):
        return self._remain_amount_currency

    @remain_amount_currency.setter
    def remain_amount_currency(self, value):
        self._remain_amount_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_budget_apply_code:
            if hasattr(self.biz_budget_apply_code, 'to_alipay_dict'):
                params['biz_budget_apply_code'] = self.biz_budget_apply_code.to_alipay_dict()
            else:
                params['biz_budget_apply_code'] = self.biz_budget_apply_code
        if self.consumed_amount:
            if hasattr(self.consumed_amount, 'to_alipay_dict'):
                params['consumed_amount'] = self.consumed_amount.to_alipay_dict()
            else:
                params['consumed_amount'] = self.consumed_amount
        if self.consumed_amount_currency:
            if hasattr(self.consumed_amount_currency, 'to_alipay_dict'):
                params['consumed_amount_currency'] = self.consumed_amount_currency.to_alipay_dict()
            else:
                params['consumed_amount_currency'] = self.consumed_amount_currency
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        if self.remain_amount_currency:
            if hasattr(self.remain_amount_currency, 'to_alipay_dict'):
                params['remain_amount_currency'] = self.remain_amount_currency.to_alipay_dict()
            else:
                params['remain_amount_currency'] = self.remain_amount_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizBudgetApplyAmountDTO()
        if 'biz_budget_apply_code' in d:
            o.biz_budget_apply_code = d['biz_budget_apply_code']
        if 'consumed_amount' in d:
            o.consumed_amount = d['consumed_amount']
        if 'consumed_amount_currency' in d:
            o.consumed_amount_currency = d['consumed_amount_currency']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        if 'remain_amount_currency' in d:
            o.remain_amount_currency = d['remain_amount_currency']
        return o


