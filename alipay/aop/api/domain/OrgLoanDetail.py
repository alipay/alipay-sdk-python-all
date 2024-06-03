#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgLoanDetail(object):

    def __init__(self):
        self._credit_amt = None
        self._is_main_product = None
        self._loan_amt = None
        self._loan_date = None
        self._loan_rate = None
        self._loan_term = None
        self._loan_term_unit = None
        self._org_drawdown_no = None
        self._repay_type = None

    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
    @property
    def is_main_product(self):
        return self._is_main_product

    @is_main_product.setter
    def is_main_product(self, value):
        self._is_main_product = value
    @property
    def loan_amt(self):
        return self._loan_amt

    @loan_amt.setter
    def loan_amt(self, value):
        self._loan_amt = value
    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, value):
        self._loan_date = value
    @property
    def loan_rate(self):
        return self._loan_rate

    @loan_rate.setter
    def loan_rate(self, value):
        self._loan_rate = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def org_drawdown_no(self):
        return self._org_drawdown_no

    @org_drawdown_no.setter
    def org_drawdown_no(self, value):
        self._org_drawdown_no = value
    @property
    def repay_type(self):
        return self._repay_type

    @repay_type.setter
    def repay_type(self, value):
        self._repay_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_amt:
            if hasattr(self.credit_amt, 'to_alipay_dict'):
                params['credit_amt'] = self.credit_amt.to_alipay_dict()
            else:
                params['credit_amt'] = self.credit_amt
        if self.is_main_product:
            if hasattr(self.is_main_product, 'to_alipay_dict'):
                params['is_main_product'] = self.is_main_product.to_alipay_dict()
            else:
                params['is_main_product'] = self.is_main_product
        if self.loan_amt:
            if hasattr(self.loan_amt, 'to_alipay_dict'):
                params['loan_amt'] = self.loan_amt.to_alipay_dict()
            else:
                params['loan_amt'] = self.loan_amt
        if self.loan_date:
            if hasattr(self.loan_date, 'to_alipay_dict'):
                params['loan_date'] = self.loan_date.to_alipay_dict()
            else:
                params['loan_date'] = self.loan_date
        if self.loan_rate:
            if hasattr(self.loan_rate, 'to_alipay_dict'):
                params['loan_rate'] = self.loan_rate.to_alipay_dict()
            else:
                params['loan_rate'] = self.loan_rate
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.org_drawdown_no:
            if hasattr(self.org_drawdown_no, 'to_alipay_dict'):
                params['org_drawdown_no'] = self.org_drawdown_no.to_alipay_dict()
            else:
                params['org_drawdown_no'] = self.org_drawdown_no
        if self.repay_type:
            if hasattr(self.repay_type, 'to_alipay_dict'):
                params['repay_type'] = self.repay_type.to_alipay_dict()
            else:
                params['repay_type'] = self.repay_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgLoanDetail()
        if 'credit_amt' in d:
            o.credit_amt = d['credit_amt']
        if 'is_main_product' in d:
            o.is_main_product = d['is_main_product']
        if 'loan_amt' in d:
            o.loan_amt = d['loan_amt']
        if 'loan_date' in d:
            o.loan_date = d['loan_date']
        if 'loan_rate' in d:
            o.loan_rate = d['loan_rate']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'org_drawdown_no' in d:
            o.org_drawdown_no = d['org_drawdown_no']
        if 'repay_type' in d:
            o.repay_type = d['repay_type']
        return o


