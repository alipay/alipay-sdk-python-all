#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditResult(object):

    def __init__(self):
        self._credit_line = None
        self._credit_no = None
        self._credit_term = None
        self._credit_term_unit = None
        self._effective_date = None
        self._expire_date = None
        self._fee_rate = None
        self._interest_rate = None
        self._loan_term = None
        self._loan_term_unit = None
        self._repayment_mode = None

    @property
    def credit_line(self):
        return self._credit_line

    @credit_line.setter
    def credit_line(self, value):
        self._credit_line = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def credit_term(self):
        return self._credit_term

    @credit_term.setter
    def credit_term(self, value):
        self._credit_term = value
    @property
    def credit_term_unit(self):
        return self._credit_term_unit

    @credit_term_unit.setter
    def credit_term_unit(self, value):
        self._credit_term_unit = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def fee_rate(self):
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, value):
        self._fee_rate = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
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
    def repayment_mode(self):
        return self._repayment_mode

    @repayment_mode.setter
    def repayment_mode(self, value):
        self._repayment_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_line:
            if hasattr(self.credit_line, 'to_alipay_dict'):
                params['credit_line'] = self.credit_line.to_alipay_dict()
            else:
                params['credit_line'] = self.credit_line
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.credit_term:
            if hasattr(self.credit_term, 'to_alipay_dict'):
                params['credit_term'] = self.credit_term.to_alipay_dict()
            else:
                params['credit_term'] = self.credit_term
        if self.credit_term_unit:
            if hasattr(self.credit_term_unit, 'to_alipay_dict'):
                params['credit_term_unit'] = self.credit_term_unit.to_alipay_dict()
            else:
                params['credit_term_unit'] = self.credit_term_unit
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.fee_rate:
            if hasattr(self.fee_rate, 'to_alipay_dict'):
                params['fee_rate'] = self.fee_rate.to_alipay_dict()
            else:
                params['fee_rate'] = self.fee_rate
        if self.interest_rate:
            if hasattr(self.interest_rate, 'to_alipay_dict'):
                params['interest_rate'] = self.interest_rate.to_alipay_dict()
            else:
                params['interest_rate'] = self.interest_rate
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
        if self.repayment_mode:
            if hasattr(self.repayment_mode, 'to_alipay_dict'):
                params['repayment_mode'] = self.repayment_mode.to_alipay_dict()
            else:
                params['repayment_mode'] = self.repayment_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditResult()
        if 'credit_line' in d:
            o.credit_line = d['credit_line']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'credit_term' in d:
            o.credit_term = d['credit_term']
        if 'credit_term_unit' in d:
            o.credit_term_unit = d['credit_term_unit']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'fee_rate' in d:
            o.fee_rate = d['fee_rate']
        if 'interest_rate' in d:
            o.interest_rate = d['interest_rate']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'repayment_mode' in d:
            o.repayment_mode = d['repayment_mode']
        return o


