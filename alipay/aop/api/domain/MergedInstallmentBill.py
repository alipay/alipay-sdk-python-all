#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MergedInstallmentBill(object):

    def __init__(self):
        self._accounting_date = None
        self._installment_end_date = None
        self._unpaid_interest = None
        self._unpaid_penalty = None
        self._unpaid_principal = None
        self._unpaid_total_amount = None

    @property
    def accounting_date(self):
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, value):
        self._accounting_date = value
    @property
    def installment_end_date(self):
        return self._installment_end_date

    @installment_end_date.setter
    def installment_end_date(self, value):
        self._installment_end_date = value
    @property
    def unpaid_interest(self):
        return self._unpaid_interest

    @unpaid_interest.setter
    def unpaid_interest(self, value):
        self._unpaid_interest = value
    @property
    def unpaid_penalty(self):
        return self._unpaid_penalty

    @unpaid_penalty.setter
    def unpaid_penalty(self, value):
        self._unpaid_penalty = value
    @property
    def unpaid_principal(self):
        return self._unpaid_principal

    @unpaid_principal.setter
    def unpaid_principal(self, value):
        self._unpaid_principal = value
    @property
    def unpaid_total_amount(self):
        return self._unpaid_total_amount

    @unpaid_total_amount.setter
    def unpaid_total_amount(self, value):
        self._unpaid_total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_date:
            if hasattr(self.accounting_date, 'to_alipay_dict'):
                params['accounting_date'] = self.accounting_date.to_alipay_dict()
            else:
                params['accounting_date'] = self.accounting_date
        if self.installment_end_date:
            if hasattr(self.installment_end_date, 'to_alipay_dict'):
                params['installment_end_date'] = self.installment_end_date.to_alipay_dict()
            else:
                params['installment_end_date'] = self.installment_end_date
        if self.unpaid_interest:
            if hasattr(self.unpaid_interest, 'to_alipay_dict'):
                params['unpaid_interest'] = self.unpaid_interest.to_alipay_dict()
            else:
                params['unpaid_interest'] = self.unpaid_interest
        if self.unpaid_penalty:
            if hasattr(self.unpaid_penalty, 'to_alipay_dict'):
                params['unpaid_penalty'] = self.unpaid_penalty.to_alipay_dict()
            else:
                params['unpaid_penalty'] = self.unpaid_penalty
        if self.unpaid_principal:
            if hasattr(self.unpaid_principal, 'to_alipay_dict'):
                params['unpaid_principal'] = self.unpaid_principal.to_alipay_dict()
            else:
                params['unpaid_principal'] = self.unpaid_principal
        if self.unpaid_total_amount:
            if hasattr(self.unpaid_total_amount, 'to_alipay_dict'):
                params['unpaid_total_amount'] = self.unpaid_total_amount.to_alipay_dict()
            else:
                params['unpaid_total_amount'] = self.unpaid_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MergedInstallmentBill()
        if 'accounting_date' in d:
            o.accounting_date = d['accounting_date']
        if 'installment_end_date' in d:
            o.installment_end_date = d['installment_end_date']
        if 'unpaid_interest' in d:
            o.unpaid_interest = d['unpaid_interest']
        if 'unpaid_penalty' in d:
            o.unpaid_penalty = d['unpaid_penalty']
        if 'unpaid_principal' in d:
            o.unpaid_principal = d['unpaid_principal']
        if 'unpaid_total_amount' in d:
            o.unpaid_total_amount = d['unpaid_total_amount']
        return o


