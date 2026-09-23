#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmountDetail(object):

    def __init__(self):
        self._amount_total = None
        self._benefit_amount = None
        self._credit_principal_amount = None
        self._marketing_amount = None
        self._principal_amount = None

    @property
    def amount_total(self):
        return self._amount_total

    @amount_total.setter
    def amount_total(self, value):
        self._amount_total = value
    @property
    def benefit_amount(self):
        return self._benefit_amount

    @benefit_amount.setter
    def benefit_amount(self, value):
        self._benefit_amount = value
    @property
    def credit_principal_amount(self):
        return self._credit_principal_amount

    @credit_principal_amount.setter
    def credit_principal_amount(self, value):
        self._credit_principal_amount = value
    @property
    def marketing_amount(self):
        return self._marketing_amount

    @marketing_amount.setter
    def marketing_amount(self, value):
        self._marketing_amount = value
    @property
    def principal_amount(self):
        return self._principal_amount

    @principal_amount.setter
    def principal_amount(self, value):
        self._principal_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_total:
            if hasattr(self.amount_total, 'to_alipay_dict'):
                params['amount_total'] = self.amount_total.to_alipay_dict()
            else:
                params['amount_total'] = self.amount_total
        if self.benefit_amount:
            if hasattr(self.benefit_amount, 'to_alipay_dict'):
                params['benefit_amount'] = self.benefit_amount.to_alipay_dict()
            else:
                params['benefit_amount'] = self.benefit_amount
        if self.credit_principal_amount:
            if hasattr(self.credit_principal_amount, 'to_alipay_dict'):
                params['credit_principal_amount'] = self.credit_principal_amount.to_alipay_dict()
            else:
                params['credit_principal_amount'] = self.credit_principal_amount
        if self.marketing_amount:
            if hasattr(self.marketing_amount, 'to_alipay_dict'):
                params['marketing_amount'] = self.marketing_amount.to_alipay_dict()
            else:
                params['marketing_amount'] = self.marketing_amount
        if self.principal_amount:
            if hasattr(self.principal_amount, 'to_alipay_dict'):
                params['principal_amount'] = self.principal_amount.to_alipay_dict()
            else:
                params['principal_amount'] = self.principal_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmountDetail()
        if 'amount_total' in d:
            o.amount_total = d['amount_total']
        if 'benefit_amount' in d:
            o.benefit_amount = d['benefit_amount']
        if 'credit_principal_amount' in d:
            o.credit_principal_amount = d['credit_principal_amount']
        if 'marketing_amount' in d:
            o.marketing_amount = d['marketing_amount']
        if 'principal_amount' in d:
            o.principal_amount = d['principal_amount']
        return o


