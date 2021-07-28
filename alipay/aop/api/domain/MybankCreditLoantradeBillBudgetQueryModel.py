#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoney import MultiCurrencyMoney
from alipay.aop.api.domain.UserVo import UserVo


class MybankCreditLoantradeBillBudgetQueryModel(object):

    def __init__(self):
        self._apply_amount = None
        self._bill_no = None
        self._out_request_no = None
        self._product_code = None
        self._repay_budget_type = None
        self._user = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        if isinstance(value, MultiCurrencyMoney):
            self._apply_amount = value
        else:
            self._apply_amount = MultiCurrencyMoney.from_alipay_dict(value)
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repay_budget_type(self):
        return self._repay_budget_type

    @repay_budget_type.setter
    def repay_budget_type(self, value):
        self._repay_budget_type = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, UserVo):
            self._user = value
        else:
            self._user = UserVo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repay_budget_type:
            if hasattr(self.repay_budget_type, 'to_alipay_dict'):
                params['repay_budget_type'] = self.repay_budget_type.to_alipay_dict()
            else:
                params['repay_budget_type'] = self.repay_budget_type
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeBillBudgetQueryModel()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repay_budget_type' in d:
            o.repay_budget_type = d['repay_budget_type']
        if 'user' in d:
            o.user = d['user']
        return o


