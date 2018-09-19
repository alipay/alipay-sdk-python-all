#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RepayDetail(object):

    def __init__(self):
        self._capital_amount = None
        self._contract_no = None
        self._interest_amount = None
        self._loan_year = None
        self._total_amount = None

    @property
    def capital_amount(self):
        return self._capital_amount

    @capital_amount.setter
    def capital_amount(self, value):
        self._capital_amount = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value
    @property
    def interest_amount(self):
        return self._interest_amount

    @interest_amount.setter
    def interest_amount(self, value):
        self._interest_amount = value
    @property
    def loan_year(self):
        return self._loan_year

    @loan_year.setter
    def loan_year(self, value):
        self._loan_year = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.capital_amount:
            if hasattr(self.capital_amount, 'to_alipay_dict'):
                params['capital_amount'] = self.capital_amount.to_alipay_dict()
            else:
                params['capital_amount'] = self.capital_amount
        if self.contract_no:
            if hasattr(self.contract_no, 'to_alipay_dict'):
                params['contract_no'] = self.contract_no.to_alipay_dict()
            else:
                params['contract_no'] = self.contract_no
        if self.interest_amount:
            if hasattr(self.interest_amount, 'to_alipay_dict'):
                params['interest_amount'] = self.interest_amount.to_alipay_dict()
            else:
                params['interest_amount'] = self.interest_amount
        if self.loan_year:
            if hasattr(self.loan_year, 'to_alipay_dict'):
                params['loan_year'] = self.loan_year.to_alipay_dict()
            else:
                params['loan_year'] = self.loan_year
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayDetail()
        if 'capital_amount' in d:
            o.capital_amount = d['capital_amount']
        if 'contract_no' in d:
            o.contract_no = d['contract_no']
        if 'interest_amount' in d:
            o.interest_amount = d['interest_amount']
        if 'loan_year' in d:
            o.loan_year = d['loan_year']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


