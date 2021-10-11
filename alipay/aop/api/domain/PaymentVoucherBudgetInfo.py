#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentVoucherRechargeInfo import PaymentVoucherRechargeInfo


class PaymentVoucherBudgetInfo(object):

    def __init__(self):
        self._amount = None
        self._budget_type = None
        self._recharge_info = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def recharge_info(self):
        return self._recharge_info

    @recharge_info.setter
    def recharge_info(self, value):
        if isinstance(value, PaymentVoucherRechargeInfo):
            self._recharge_info = value
        else:
            self._recharge_info = PaymentVoucherRechargeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.recharge_info:
            if hasattr(self.recharge_info, 'to_alipay_dict'):
                params['recharge_info'] = self.recharge_info.to_alipay_dict()
            else:
                params['recharge_info'] = self.recharge_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentVoucherBudgetInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'recharge_info' in d:
            o.recharge_info = d['recharge_info']
        return o


